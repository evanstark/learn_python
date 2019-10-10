#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# @File Name    : 摇骰子_输赢概率.py
# @Description  :
# @Author       : EvanStark
# @E-mail       : evanstark@aliyun.com
# @Creation Time: 2019/10/10  22:39
# @Software     : PyCharm
# --------------------------------------------------

import random

POINT = 11

def shake_the_dice(times): # 摇的点数刚好等于POINT时，该局不算，重新摇！
    small = 0
    draw = 0
    big = 0
    i = 0
    while i < times:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        if a == b == c:
            draw += 1
        elif a + b + c < POINT:
            small += 1
        elif a + b + c > POINT:
            big += 1
        else:
            continue
        i += 1
    print('''
    摇骰子总次数：%d,
    判断大小点数：%d,
    开大次数：%d,
    开小次数：%d,
    三同次数：%d,
    ''' % (times, POINT, big, small, draw))

def shake_the_dice2(times): # 摇的点数刚好等于POINT时，该局算大赢！
    small = 0
    draw = 0
    big = 0
    i = 0
    while i < times:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        if a == b == c:
            draw += 1
        elif a + b + c < POINT:
            small += 1
        # elif a + b + c > POINT: big += 1
        else:
            big += 1
        i += 1
    print('''
    摇骰子总次数：%d,
    判断大小点数：%d,
    开大次数：%d,
    开小次数：%d,
    三同次数：%d,
    ''' % (times, POINT, big, small, draw))

if __name__ == '__main__':
    shake_the_dice2(5000)