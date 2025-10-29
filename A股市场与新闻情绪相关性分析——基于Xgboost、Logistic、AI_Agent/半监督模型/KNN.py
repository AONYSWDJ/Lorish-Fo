import numpy as np
import pandas as pd
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from scipy.sparse import hstack, csr_matrix

class KNNIterativeLabelerSparse:
    def __init__(self, k=5):
        self.k = k
        self.vectorizer = TfidfVectorizer(tokenizer=self.jieba_tokenizer)
        self.scaler = StandardScaler()
        self.knn = None
        self.train_X = None  # csr_matrix
        self.train_y = None

    @staticmethod
    def jieba_tokenizer(text):
        return list(jieba.cut(text))

    def fit(self, train_df: pd.DataFrame, text_col: str, extra_features: list, label_col: str):
        tfidf_matrix = self.vectorizer.fit_transform(train_df[text_col])
        extra_matrix = csr_matrix(self.scaler.fit_transform(train_df[extra_features]))
        X = hstack([tfidf_matrix, extra_matrix])
        y = train_df[label_col].values
        self.train_X = X
        self.train_y = y
        self.knn = KNeighborsClassifier(n_neighbors=self.k, n_jobs=-1)
        self.knn.fit(X, y)

    def predict(self, df: pd.DataFrame, text_col: str, extra_features: list):
        tfidf_matrix = self.vectorizer.transform(df[text_col])
        extra_matrix = csr_matrix(self.scaler.transform(df[extra_features]))
        X = hstack([tfidf_matrix, extra_matrix])
        return self.knn.predict(X)

    def evaluate(self, df: pd.DataFrame, text_col: str, extra_features: list, label_col: str):
        y_pred = self.predict(df, text_col, extra_features)
        y_true = df[label_col].values
        acc = accuracy_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred, average='weighted')
        return acc, f1

    def iterative_labeling(self, test_df: pd.DataFrame, val_df: pd.DataFrame,
                           text_col: str, extra_features: list, label_col: str,
                           threshold=0.9, max_iter=5):
        """
        迭代标注未标注样本，并在验证集上监控准确率和 F1-score
        """
        for i in range(max_iter):
            print(f"\n=== Iteration {i+1} ===")
            if hasattr(self.knn, "predict_proba"):
                tfidf_matrix = self.vectorizer.transform(test_df[text_col])
                extra_matrix = csr_matrix(self.scaler.transform(test_df[extra_features]))
                X_test = hstack([tfidf_matrix, extra_matrix])
                probs = self.knn.predict_proba(X_test)
                max_probs = probs.max(axis=1)
                confident_idx = np.where(max_probs >= threshold)[0]

                if len(confident_idx) == 0:
                    print("No confident samples to add. Stopping iteration.")
                    break

                # 高置信度样本加入训练集
                new_X = X_test[confident_idx]
                new_y = self.knn.predict(new_X)

                # 拼接到现有训练集
                self.train_X = hstack([self.train_X, new_X]) if self.train_X.shape[1] != new_X.shape[1] else vstack([self.train_X, new_X])
                self.train_y = np.hstack([self.train_y, new_y])

                # 重新训练 KNN
                self.knn.fit(self.train_X, self.train_y)

                # 从测试集删除已标注样本
                test_df = test_df.drop(test_df.index[confident_idx])

                # 验证集评估
                acc, f1 = self.evaluate(val_df, text_col, extra_features, label_col)
                print(f"Added {len(confident_idx)} samples to training set.")
                print(f"Validation Accuracy: {acc:.4f}, F1-score: {f1:.4f}")

            else:
                print("KNN does not support predict_proba. Use k>1 and default settings.")
                break
