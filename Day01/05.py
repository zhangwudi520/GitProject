# -*- coding:utf-8 -*-
import random

__author__ = 'zdt'
__date__ = '2019/10/22 19:33'


def add(*args):
    """
    可变参数的运用
    :param args:
    :return:
    """
    t = 0
    for _ in args:  # 此处传过来几个值，进行几次循环
        t += random.randint(1, 6)
        print(t)
    print('----------')


if __name__ == '__main__':
    add()
    add(1)
    add(1, 2)
    add(1, 2, 3)
