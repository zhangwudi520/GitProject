# -*- coding:utf-8 -*-
__author__ = 'zdt'
__date__ = '2019/10/22 15:56'


def main():
    """
    求水仙花数
    //  整除
    /   除
    %   取余
    :return:
    """
    for i in range(123, 1000):
        best = i // 100
        ten = i // 10 % 10
        a = i % 10
        if best ** 3 + ten ** 3 + a ** 3 == i:
            print(i)


if __name__ == '__main__':
    main()
