# -*- coding:utf-8 -*-
import random

__author__ = 'zdt'
__date__ = '2019/10/22 20:51'
import os
import time


def max_max2(x):
    """
    返回传入函数的列表的最大两个值
    :param x:
    :return:
    """
    xx = sorted(x)
    print(xx[-1], xx[-2])


def code():
    """
    使用ASCII码生成字母数字列表，再随机生成给定长度的验证码
    :return:
    """
    lens = int(input("Input a int num:"))
    codes = ''
    num_ascii = [chr(n) for n in range(48, 58)]
    word_ascii = [chr(m) for m in range(65, 91)]
    words_ascii = [chr(m) for m in range(97, 122)]
    ascii_l = num_ascii + word_ascii + words_ascii

    for _ in range(lens):
        # random.choice()函数，随机从列表中获取一个值
        codes += random.choice(ascii_l)
    print(codes)


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')
        # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    # main()
    # code()
    max_max2([1, 2, 3, 4, 5])
