from langchain_community.chat_models import ChatTongyi
from langchain.agents import initialize_agent, Tool
from langchain.prompts import PromptTemplate
from .MCP_Tool.csv_utils import add_sentiment_column
import pandas as pd
import os
from dotenv import load_dotenv

# ========== 基本参数 ==========
CSV_PATH = r"C:\Users\20429\Desktop\国泰君安期货笔试\data\HIC_Data.csv"
TEXT_COLUMN = "content"
BATCH_SIZE = 5  # 调小批量，防止模型卡住
TEMPERATURE = 0

# 加载 API key
load_dotenv(r"C:\Users\20429\Desktop\国泰君安期货笔试\agent识别\keys.env")
tongyi_api_key = os.getenv("tongyi_api_key".upper())

# 初始化模型
llm = ChatTongyi(model="qwen-max", dashscope_api_key=tongyi_api_key, temperature=TEMPERATURE)

# 定义 MCP 工具
tools = [
    Tool(
        name="add_sentiment_column",
        func=add_sentiment_column,
        description="向CSV文件添加情感分析结果列并保存新文件"
    )
]

# 初始化 Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",
    verbose=False
)

# Prompt 模板
prompt_template = "判断以下句子的情感倾向，正面返回1，负面返回0。只返回数字列表，例如 [1,0,1]。\n{texts}"

# ========== 核心函数 ==========
def analyze_csv(csv_path: str):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"文件不存在: {csv_path}")

    df = pd.read_csv(csv_path)
    if TEXT_COLUMN not in df.columns:
        raise ValueError(f"文件中找不到列：{TEXT_COLUMN}")

    sentiments = []

    for i in range(0, len(df), BATCH_SIZE):
        batch = df[TEXT_COLUMN].iloc[i:i+BATCH_SIZE].astype(str).tolist()
        # 截断过长文本，保证稳定
        batch = [t[:500] for t in batch]

        prompt = prompt_template.format(texts="\n".join(batch))

        # 调用模型并捕获异常
        try:
            result = llm.invoke(prompt)
            raw_output = str(result.content).strip()
            batch_values = eval(raw_output)
            if not isinstance(batch_values, list):
                raise ValueError
            batch_values = [int(v) if v in [0, 1] else 0 for v in batch_values]
        except Exception:
            # 出错时，回退为单条调用
            batch_values = []
            for text in batch:
                try:
                    res = llm.invoke(f"判断情感正负，正面返回1，负面返回0，只输出数字。\n{text[:500]}")
                    val = int(str(res.content).strip())
                    val = val if val in [0, 1] else 0
                except:
                    val = 0
                batch_values.append(val)

        # 控制台输出
        print("\n=== 批次结果 ===")
        for text, val in zip(batch, batch_values):
            print(f"📝 文本: {text[:50]}...")
            print(f"→ 判断结果: {val}\n")

        sentiments.extend(batch_values)
        print(f"已处理 {i + len(batch)}/{len(df)} 条")

    # 调用 MCP 工具保存 CSV
    new_file = add_sentiment_column(csv_path, sentiments)
    print(f"\n🎯 全部完成！新文件已保存: {new_file}")


if __name__ == "__main__":
    analyze_csv(CSV_PATH)
