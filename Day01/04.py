# -*- coding:utf-8 -*-
__author__ = 'zdt'
__date__ = '2019/10/22 19:24'


def factorial(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数,也就是from math import factorial
print(factorial(m) // factorial(n) // factorial(m - n))
