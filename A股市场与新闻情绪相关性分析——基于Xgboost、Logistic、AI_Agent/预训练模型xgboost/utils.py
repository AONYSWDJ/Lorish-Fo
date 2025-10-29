# -*- coding: utf-8 -*-
import jieba
import re
import pandas as pd

stopwords = []
with open(r"C:\Users\20429\Desktop\国泰君安期货笔试\预训练模型xgboost\data\stopwords.txt", "r", encoding="utf8") as f:
    for w in f:
        stopwords.append(w.strip())


def load_corpus(path):
    """
    加载语料库
    """
    data = pd.read_csv(path, encoding="utf-8")
    data = data[['content','label']]
    data.dropna(inplace=True,axis=0)
    data['content'] = data['content'].apply(processing)
    return data
# ------------------ 文本处理函数 ------------------
def processing(text):


    text = text.replace('\n', ' ').replace('\r', ' ').strip()

    # 去掉标点符号（保留中文、英文、数字）
    text = re.sub(r'[^\w\u4e00-\u9fff]', ' ', text)

    # 分词
    words = jieba.lcut(text)

    # 去停词 & 空字符串
    words = [w for w in words if w and w not in stopwords]

    return ' '.join(words)


# def load_corpus(path):
#     """
#     加载语料库
#     """
#     data = []
#     i = 0
#     with open(path, "r", encoding="utf8") as f:
#         for line in f:
#             line = line.strip()
#             if not line:  # 跳过空行
#                 continue
#             parts = line.rsplit(",", 2)  # 从右边最多分割两次
#             if len(parts) < 2:
#                 print("格式异常行，已跳过：", line)
#                 continue
#             seniment, content = parts[-2], parts[-1]
#             try:
#                 data.append((processing(content), int(seniment)))
#             except ValueError:
#                 print("情感标签非数字行，已跳过：", line)
#     return data




#
# def processing(text):
#     """
#     数据预处理, 可以根据自己的需求进行重载
#     """
#     # 数据清洗部分
#     text = re.sub("\{%.+?%\}", " ", text)           # 去除 {%xxx%} (地理定位, 微博话题等)
#     text = re.sub("@.+?( |$)", " ", text)           # 去除 @xxx (用户名)
#     text = re.sub("【.+?】", " ", text)              # 去除 【xx】 (里面的内容通常都不是用户自己写的)
#     text = re.sub("\u200b", " ", text)              # '\u200b'是这个数据集中的一个bad case, 不用特别在意
#     # 分词
#     words = [w for w in jieba.lcut(text) if w.isalpha()]
#     # 对否定词`不`做特殊处理: 与其后面的词进行拼接
#     while "不" in words:
#         index = words.index("不")
#         if index == len(words) - 1:
#             break
#         words[index: index+2] = ["".join(words[index: index+2])]  # 列表切片赋值的酷炫写法
#     # 用空格拼接成字符串
#     result = " ".join(words)
#     return result


# def processing_bert(text):
#     """
#     数据预处理, 可以根据自己的需求进行重载
#     """
#     # 数据清洗部分
#     text = re.sub("\{%.+?%\}", " ", text)           # 去除 {%xxx%} (地理定位, 微博话题等)
#     text = re.sub("@.+?( |$)", " ", text)           # 去除 @xxx (用户名)
#     text = re.sub("【.+?】", " ", text)              # 去除 【xx】 (里面的内容通常都不是用户自己写的)
#     text = re.sub("\u200b", " ", text)              # '\u200b'是这个数据集中的一个bad case, 不用特别在意
#     return text