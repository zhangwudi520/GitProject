# -*- coding:utf-8 -*-
__author__ = 'zdt'
__date__ = '2019/10/22 20:09'


def fav(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    """
    使用yield，递归生成斐波那契数列
    :return:
    """
    n = int(input("xxxxxxx:  "))
    for x in fav(n):
        print(x)


if __name__ == '__main__':
    main()
