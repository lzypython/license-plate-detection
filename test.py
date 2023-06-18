#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：code 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：咋
@Date    ：2023/4/20 11:16 
"""
# import torch
# print(torch.cuda.is_available())
# print(torch.__version__)
import cv2
from add import add_str
image = cv2.imread("images/tmp/single_result.jpg")
print(image.shape)
image = add_str(image, "123", 0, 0, (0, 0, 255, 0))
print(image.shape)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
