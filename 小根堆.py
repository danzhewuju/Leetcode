#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 10:28 上午
# @Author  : Alex
# @Site    : 
# @File    : 小根堆.py
# @Software: PyCharm
import random
import numpy as np


class Heap:
    def __init__(self, K, data):
        # 堆的初始化
        self.heaq = []
        self.max_size = K
        if len(data) <= K:
            self.heaq = data
        else:
            self.heaq = data[:K]
        # 初始化
        for i in range(len(self.heaq) // 2, -1, -1):
            self.init_heaq(i)
        if len(data) > K:
            for d in data[K:]:
                self.add_new_num(d)

    def add_new_num(self, d):
        if d > self.heaq[0]:
            self.heaq[0] = d
            self.init_heaq(0)

    def init_heaq(self, k):
        max_value = k
        if 2 * k + 1 < len(self.heaq) and self.heaq[max_value] > self.heaq[2 * k + 1]:
            max_value = 2 * k + 1
        if 2 * k + 2 < len(self.heaq) and self.heaq[max_value] > self.heaq[2 * k + 2]:
            max_value = 2 * k + 2
        if max_value != k:
            tmp = self.heaq[max_value]
            self.heaq[max_value] = self.heaq[k]
            self.heaq[k] = tmp
            self.init_heaq(max_value)
        return

    def get_heaq(self):
        return self.heaq


a = np.random.randint(0, 100, 10).tolist()
print(a)
heaq = Heap(5, a)
a.sort(reverse = True)
print(a)
print(heaq.get_heaq())
