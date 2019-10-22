# -*- coding:utf-8 -*-
from math import sqrt

__author__ = 'zdt'
__date__ = '2019/10/22 15:35'


def main():
    """
    判断输入数字以内的素数
    :return:
    """
    num = int(input("Input a int num:"))
    prime_true = []
    prime_false = []
    while num > 1:
        end = int(sqrt(num))
        is_prime = True

        for x in range(2, end + 1):
            if num % x == 0:
                is_prime = False
                break

        if is_prime and num != 1:
            prime_true.append(num)
        else:
            prime_false.append(num)
        num -= 1
    print("Prime is {t},\nNot Prime is {f}".format(t=prime_true, f=prime_false))


if __name__ == '__main__':
    main()

