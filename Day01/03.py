# -*- coding:utf-8 -*-
from math import sqrt

__author__ = 'zdt'
__date__ = '2019/10/22 16:29'


def fibonacci():
    """
    斐波那契数列
    :return:
    """
    num = int(input("Input a int num:"))
    fi = []
    for i in range(2, num):
        if len(fi) < 2:
            fi = [1, 1]
        fi.append(fi[-2] + fi[-1])
    print(fi)


def perfect():
    """
    求完美数
    :return:
    """
    num = int(input("Input a int num:"))
    while num > 1:
        p = [1]
        for i in range(2, num):
            if num % i == 0:
                p.append(i)

        if sum(p) == num:
            # 使用sum()函数求列表和
            print(num)
        num -= 1


if __name__ == '__main__':
    # fibonacci()
    perfect()
