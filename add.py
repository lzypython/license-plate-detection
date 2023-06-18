#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：code 
@File    ：add.py
@IDE     ：PyCharm 
@Author  ：咋
@Date    ：2023/4/20 14:07 
"""
import numpy as np
from PIL import ImageFont,ImageDraw,Image
def add_str(image,match_str,x,y,fill):
    font = ImageFont.truetype("msyh.ttc",80)  # 数字代表字体大小
    # 创建一个pillow的图片
    pil_img = Image.fromarray(image)
    # 绘制图片
    draw = ImageDraw.Draw(pil_img)
    # 利用draw去绘制中文
    draw.text((x,y), match_str , font=font, fill=fill)  # 后面的fill即颜色，RGBA
    # 重新变为ndarray
    image = np.array(pil_img)
    return image