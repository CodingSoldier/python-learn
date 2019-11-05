# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt
from collections import Counter

def knn_classify(k, X_train, y_train, x):

    assert 1 <= k <= X_train.shape[0], "k要大于等于1，小于等于数组X_train第一维大小"
    assert X_train.shape[0] == y_train.shape[0], "数组X_train第一维大小要等于数组y_train第一维大小"
    assert X_train.shape[1] == x.shape[0], "数组X_train第二维大小要等于预测点x第一维大小"

    distances = [sqrt(np.sum((dot -x)**2)) for dot in X_train]
    nearest = np.argsort(distances)

    top_k_y = [y_train[i] for i in nearest[:k]]
    votes = Counter(top_k_y)

    return votes.most_common(1)[0][0]

