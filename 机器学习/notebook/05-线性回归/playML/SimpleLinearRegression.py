import numpy as np

class SimpleLinearRegression1:

    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        assert x_train.ndim == 1, \
            "线性回归只能解决单特征训练数据"
        assert len(x_train) == len(y_train), \
            "x_train、y_train的维度必须一样"

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = 0.0
        d = 0.0

        for x, y in zip(x_train, y_train):
            num += (x - x_mean) * (y - y_mean)
            d += (x - x_mean) ** 2

        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

        return self

    def predict(self, x_predict):
        assert x_predict.ndim == 1, \
            "线性回归只能解决单特征问题"
        assert self.a_ is not None and self.b_ is not None, \
            "必须先调用fit"

        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x_single):
        return self.a_ * x_single + self.b_


# 向量化
class SimpleLinearRegression2:

    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        assert x_train.ndim == 1, \
            "线性回归只能解决单特征训练数据"
        assert len(x_train) == len(y_train), \
            "x_train、y_train的维度必须一样"

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        # 使用向量相乘，不使用for循环，提高性能
        num = (x_train - x_mean).dot(y_train - y_mean)
        d = (x_train - x_mean).dot(x_train - x_mean)

        # for x, y in zip(x_train, y_train):
        #     num += (x - x_mean) * (y - y_mean)
        #     d += (x - x_mean) ** 2

        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

        return self

    def predict(self, x_predict):
        assert x_predict.ndim == 1, \
            "线性回归只能解决单特征问题"
        assert self.a_ is not None and self.b_ is not None, \
            "必须先调用fit"

        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x_single):
        return self.a_ * x_single + self.b_
