# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt
from collections import Counter

def knn_classify(k, x_train, y_train, x):

    assert 1 <= k <= x_train.shape[0], "k值错误"
    assert x_train.shape[0] == y_train.shape[0], "x_train维度==target的维度"
    assert x_train.shape[1] == x.shape[0], "x_train元素的维度==x的维度"

    distances = [sqrt(np.sum((dot -x)**2)) for dot in x_train]
    nearest = np.argsort(distances)

    top_k_y = [y_train[i] for i in nearest[:k]]
    votes = Counter(top_k_y)

    return votes.most_common(1)[0][0]
