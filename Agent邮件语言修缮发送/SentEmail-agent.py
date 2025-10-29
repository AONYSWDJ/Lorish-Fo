# ========================== 环境与依赖导入 ==========================
import os
from dotenv import load_dotenv
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_openai_tools_agent
import yagmail
from statsmodels.datasets.macrodata.data import variable_names


# ========================== Step 0: 环境与模型初始化 ==========================
load_dotenv()
llm = ChatTongyi(
    model='qwen-plus',
    api_key=os.getenv("DASHSCOPE_API_KEY")
)


# ========================== Step 1: 工具函数定义与注册 ==========================
@tool
def send_email(recipient: str, subject: str, content: str) -> str:
    """
    发送邮件。参数：收件人、主题、正文。
    """
    try:
        yag = yagmail.SMTP(
            user=os.getenv("EMAIL_USER"),              # 你的 Gmail 地址
            password=os.getenv("EMAIL_APP_PASSWORD"),  # 应用专用密码
            host='smtp.gmail.com',
            port=465,
            smtp_ssl=True
        )
        yag.send(to=recipient, subject=subject, contents=content)
        print(f"✅ 邮件已成功发送给 {recipient}")
    except Exception as e:
        print(f"❌ 邮件发送失败：{str(e)}")

# 工具注册绑定
tools = [send_email]
model_with_tools = llm.bind_tools(tools)


# ========================== Step 2: 提取结构化信息链 ==========================
schemas = [
    ResponseSchema(name='content', description='邮件内容'),
    ResponseSchema(name='subject', description='邮件主题'),
    ResponseSchema(name='recipient', description='收件人'),
]
parser_struct = StructuredOutputParser.from_response_schemas(schemas)

extract_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(
        "请你从以下文字中提取出邮件内容、收件人并且总结出主题，并返回JSON格式：{format_instruction}，不能擅改内容\\n输入：{text}"
    )
])
extract_chain = extract_prompt.partial(
    format_instruction=parser_struct.get_format_instructions()
) | llm | parser_struct


# ========================== Step 3: 中间处理节点 ==========================
def return_dict(s):
    print(s)
    return s
return_node = RunnableLambda(return_dict)

def extract_str(dict_mail):
    return {'dict_mail': f'{dict_mail}'}
extract_node = RunnableLambda(extract_str)


# ========================== Step 4: 优化邮件语言 ==========================
refine_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("你是一位精通语言修辞的AI助手，擅长把中文翻译成英文并进行润色和优化。"),
    HumanMessagePromptTemplate.from_template("对于接受到的字典类型的{dict_mail}，只针对这个字典中的[content]和[subject]进行语言优化，最后输出JSON格式：{format_instruction}")
])
schemas = [
    ResponseSchema(name='content', description='content'),
    ResponseSchema(name='subject', description='subject'),
    ResponseSchema(name='recipient', description='recipient'),
]
parser_struct = StructuredOutputParser.from_response_schemas(schemas)
refine_chain = refine_prompt.partial(
    format_instruction=parser_struct.get_format_instructions()
) | llm | parser_struct


# ========================== Step 5: 构建 Agent 执行链 ==========================
repack_node = RunnableLambda(lambda data: {
    'recipient': data['recipient'],
    'subject': data['subject'],
    'content': data['refined']
})

final_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "你是一个AI助手，可以使用工具如发送邮件，请根据需要使用合适的工具完成任务。同时请将邮件内容格式化为标准英文邮件格式。如果开头是称呼（如 Dear xxx,），请在称呼后添加一个换行符，使正文另起一行。"
    ),
    HumanMessagePromptTemplate.from_template("请将以下邮件发送给 {recipient}：主题是 {subject}，内容是 {content},"),
    MessagesPlaceholder(variable_name='agent_scratchpad')
])

agent = create_openai_tools_agent(
    llm=model_with_tools,
    tools=tools,
    prompt=final_prompt
)
final_agent = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

chains = extract_chain | return_node | extract_node | refine_chain | final_agent


# ========================== Step 6: 命令行入口 ==========================
if __name__ == '__main__':
    print("请输入你要发送的内容（包括主题、正文、收件人等）:")
    text = input("  ")
    result = chains.invoke({"text": text})

