#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/10/24 17:40
# @Author  : Ron
# @File    : test.py
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':


    # Simple plot with known good data
    x = np.array([1, 2, 3, 4])
    y = np.array([10, 20, 25, 30])

    plt.plot(x, y)
    plt.show()