#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：yolov5-mask-42-master 
@File    ：split.py
@IDE     ：PyCharm 
@Author  ：咋
@Date    ：2022/11/17 22:00 
"""
import cv2 as cv
def split(list_1,img,i):
    dst = img[int(list_1[1]):int(list_1[3]),int(list_1[0]):int(list_1[2])]  # 裁剪坐标为[y0:y1, x0:x1] xyxy
    cv.imwrite("1.png", dst)


# list_1 =[231,1391,586,1518]
# img = cv.imread('train_25.jpg')
# split(list_1,img,0)
