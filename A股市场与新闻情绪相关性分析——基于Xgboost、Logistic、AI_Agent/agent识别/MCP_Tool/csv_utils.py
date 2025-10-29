import pandas as pd
import os
from typing import List

def add_sentiment_column(csv_path: str, sentiments: List[int], new_col_name: str = "sentiment"):
    """
    在 csv 中增加新的列并保存为新文件（utf-8-sig）。
    要求 len(sentiments) == number of rows in csv.
    返回新文件路径。
    """
    df = pd.read_csv(csv_path)
    if len(df) != len(sentiments):
        raise ValueError(f"情感结果长度({len(sentiments)})与 CSV 行数({len(df)}) 不匹配")
    df[new_col_name] = sentiments
    base, ext = os.path.splitext(csv_path)
    new_path = f"{base}_with_sentiment{ext}"
    df.to_csv(new_path, index=False, encoding="utf-8-sig")
    return new_path
