import pandas as pd
import xgboost as xgb
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import hstack
from .utils import load_corpus, stopwords  # 调用 utils.py 里的方法和停词
import numpy as np
class XGBoostTrainer:
    def __init__(self, text_column='content', label_column='label', max_features=2000):
        self.text_column = text_column
        self.label_column = label_column
        self.max_features = max_features
        self.model = None
        self.vectorizer = None
        self.feature_names = None
        self.stopwords = stopwords  # 来自 utils.py

    # ---------------- 数据准备 ----------------
    def prepare_data(self, df, additional_features=None):
        """
        文本向量化 + 拼接额外特征
        """
        self.vectorizer = CountVectorizer(token_pattern=r'\[?\w+\]?',
                                          stop_words=self.stopwords,
                                          max_features=self.max_features)
        X_text = self.vectorizer.fit_transform(df[self.text_column])
        self.feature_names = self.vectorizer.get_feature_names_out()

        # --- 新增：处理额外特征 ---
        if additional_features is not None:
            if isinstance(additional_features, pd.DataFrame):
                X_add = additional_features.values

            elif isinstance(additional_features, (list, tuple)):
                # 如果是 [list1, list2, ...] 形式
                if all(isinstance(i, list) or isinstance(i, np.ndarray) for i in additional_features):
                    X_add = np.column_stack(additional_features)
                else:
                    # 单列 list
                    X_add = np.array(additional_features).reshape(-1, 1)
            else:
                raise ValueError("additional_features 必须是 DataFrame 或 list of list")

            X = hstack([X_text, X_add])
        else:
            X = X_text

        y = df[self.label_column].astype(int).values
        return X, y

    # ---------------- 模型训练 ----------------
    def train(self, path_or_df, additional_features=None, num_boost_round=200, params=None):
        """
        path_or_df: CSV 文件路径或者 DataFrame
        如果是路径，使用 utils.load_corpus 读取
        """
        if isinstance(path_or_df, str):
            # 调用 utils.py 里的 load_corpus
            df = load_corpus(path_or_df)
        else:
            df = path_or_df.copy()

        X, y = self.prepare_data(df, additional_features)
        dmatrix = xgb.DMatrix(X, label=y)

        if params is None:
            params = {
                'booster': 'gbtree',
                'max_depth': 6,
                'scale_pos_weight': 0.5,
                'colsample_bytree': 0.8,
                'objective': 'binary:logistic',
                'eval_metric': 'error',
                'eta': 0.3,
                'nthread': 10,
            }

        self.model = xgb.train(params, dmatrix, num_boost_round=num_boost_round)
        return self.model

    # ---------------- 预测 ----------------
    def predict(self, texts, additional_features=None):
        X_text = self.vectorizer.transform(texts)
        if additional_features is not None:
            if isinstance(additional_features, pd.DataFrame):
                X_add = additional_features.values
            else:
                X_add = additional_features
            X = hstack([X_text, X_add])
        else:
            X = X_text
        dmatrix = xgb.DMatrix(X)
        return self.model.predict(dmatrix)
