from collections import Counter

import numpy as np
from math import sqrt


class KNNClassifier:

    def __init__(self, k):
        assert k >= 1, "k必须大于等于1"
        self.k = k
        self._X_train = None
        self._y_train = None

    def fit(self, X_train, y_train):
        assert X_train.shape[0] == y_train.shape[0], "训练数据集矩阵X_train第一维大小和数组y_train第一维大小要相等"
        assert self.k <= X_train.shape[0], "k要小于训练数据集矩阵X_train第一维大小"

        self._X_train = X_train
        self._y_train = y_train
        return self

    def _predict(self, x):
        assert x.shape[0] == self._X_train.shape[1], "预测数据第一维大小要等于训练数据集矩阵的第二维大小"

        distances = [sqrt(np.sum((x_train -x) ** 2)) for x_train in self._X_train]
        nearest = np.argsort(distances)

        topK_y = [self._y_train[i] for i in nearest[:self.k]]
        votes = Counter(topK_y)

        return votes.most_common(1)[0][0]

    def predict(self, X_predict):
        assert self._X_train is not None and self._y_train is not None, "predict之前必须先fit"
        assert X_predict.shape[1] == self._X_train.shape[1], "预测数据集第二维大小要等于训练数据集矩阵_X_train第二维大小"

        y_predict = [self._predict(x) for x in X_predict]
        return np.array(y_predict)

    def __repr__(self):
        return "KNN(k=%d)" % self.k


