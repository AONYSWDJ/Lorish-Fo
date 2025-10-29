import jieba
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score
from scipy.sparse import hstack, csr_matrix


class LogisticIterativeLabeler:
    """
    半监督逻辑回归伪标签迭代器
    """

    def __init__(self, max_iter=5, confidence_threshold=0.9, max_features=5000, random_state=42):
        self.max_iter = max_iter
        self.confidence_threshold = confidence_threshold
        self.vectorizer = TfidfVectorizer(max_features=max_features)
        self.scaler = StandardScaler(with_mean=False)
        self.model = LogisticRegression(max_iter=1000, random_state=random_state)
        self.history = []

    def _prepare_features(self, df, text_col, extra_features=None, fit_vectorizer=False):
        texts = df[text_col].astype(str).apply(lambda x: ' '.join(jieba.cut(x)))

        if fit_vectorizer:
            tfidf = self.vectorizer.fit_transform(texts)
        else:
            tfidf = self.vectorizer.transform(texts)

        if extra_features:
            extra_matrix = csr_matrix(self.scaler.fit_transform(df[extra_features]))
            X = hstack([tfidf, extra_matrix])
        else:
            X = tfidf
        return X

    def fit(self, labeled_df, unlabeled_df, text_col, label_col, extra_features=None, valid_df=None):
        X_labeled = self._prepare_features(labeled_df, text_col, extra_features, fit_vectorizer=True)
        y_labeled = labeled_df[label_col].values
        X_unlabeled = self._prepare_features(unlabeled_df, text_col, extra_features)

        if valid_df is not None:
            X_valid = self._prepare_features(valid_df, text_col, extra_features)
            y_valid = valid_df[label_col].values
        else:
            X_valid, y_valid = None, None

        for iteration in range(1, self.max_iter + 1):
            print(f"Iteration {iteration}: labeled samples = {len(y_labeled)}")

            self.model.fit(X_labeled, y_labeled)
            probs = self.model.predict_proba(X_unlabeled)
            preds = self.model.predict(X_unlabeled)
            max_probs = probs.max(axis=1)

            high_conf_mask = max_probs >= self.confidence_threshold
            new_X = X_unlabeled[high_conf_mask]
            new_y = preds[high_conf_mask]

            print(f"New pseudo-labeled samples added: {new_X.shape[0]}")

            if new_X.shape[0] == 0:
                print("No high-confidence samples, stopping early.")
                break

            X_labeled = csr_matrix(np.vstack([X_labeled.toarray(), new_X.toarray()]))
            y_labeled = np.concatenate([y_labeled, new_y])
            X_unlabeled = X_unlabeled[~high_conf_mask]

            if valid_df is not None:
                y_pred_valid = self.model.predict(X_valid)
                acc = accuracy_score(y_valid, y_pred_valid)
                f1 = f1_score(y_valid, y_pred_valid, average='weighted')
                self.history.append((iteration, acc, f1))
                print(f"Validation Accuracy: {acc:.4f}, F1-score: {f1:.4f}")

        print("Training finished.")
        return self

    def evaluate(self, df, text_col, label_col, extra_features=None):
        X = self._prepare_features(df, text_col, extra_features)
        y_true = df[label_col].values
        y_pred = self.model.predict(X)
        acc = accuracy_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred, average='weighted')
        print(f"Accuracy: {acc:.4f}, F1-score: {f1:.4f}")
        return acc, f1

    def predict(self, new_test_df, text_col, extra_features=None):
        """对新的测试集进行预测，返回预测标签"""
        X_new = self._prepare_features(new_test_df, text_col, extra_features)
        pred_y = self.model.predict(X_new)
        new_test_df = new_test_df.copy()
        new_test_df["pred_label"] = pred_y
        print(f"Predicted {len(pred_y)} samples.")
        return new_test_df[["pred_label"]]
