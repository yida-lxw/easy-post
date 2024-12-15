# -*- coding: utf-8 -*-

'''
@Project  easy-post
@File     image_extract_result.py
@IDE      PyCharm
@Author   yida
@Email    949226420@qq.com
@Date     2024.12.15 15:03
@Desc     从MD文档中提取出的图片链接识别结果
'''

class ImageExtractResult:
    def __init__(self, image_label_full_text, image_name, image_file_path):
        self.image_label_full_text = image_label_full_text
        self.image_name = image_name
        self.image_file_path = image_file_path
