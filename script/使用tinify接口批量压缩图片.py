#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# @File Name    : 使用tinify接口批量压缩图片.py
# @Description  :
# @Author       : EvanStark
# @E-mail       : evanstark@aliyun.com
# @Creation Time: 2019/10/10  22:59
# @Software     : PyCharm
# --------------------------------------------------

# 参考文档：https://tinypng.com/developers/reference/python
# pip install --upgrade tinify # 安装tinify库命令

import os
import tinify

tinify.key = 'mSXSmYzRRT6yPpL7PjBGlyTmKkQX55Hj'
# tinify.key = "YOUR_API_KEY"

path = 'D:' # 图片存放的路径

def compress_img(): # 压缩图片
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            imgpath = os.path.join(dirpath, file)
            com_file = 'com_' + file
            com_imgpath = os.path.join(dirpath, com_file)
            print('compressing...' + imgpath)
            tinify.from_file(imgpath).to_file(com_imgpath)

def resizing_img(): # 调整图像大小
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            imgpath = os.path.join(dirpath, file)
            res_file = 'res_' + file
            res_imgpath = os.path.join(dirpath, res_file)
            print('resizing...' + imgpath)
            source = tinify.from_file(imgpath)
            resized = source.resize(
                method="fit", # scale\fit\cover\thumb
                width=150,
                height=100
            )
            resized.to_file(res_imgpath)

if __name__ == '__main__':
    compress_img()