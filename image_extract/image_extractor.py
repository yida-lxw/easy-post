# -*- coding: utf-8 -*-

from typing import TypeVar

from image_extract_result import ImageExtractResult

'''
@Project  easy-post
@File     image_extractor.py
@IDE      PyCharm
@Author   yida
@Email    949226420@qq.com
@Date     2024.12.14 21:21
@Desc     从MD文档中提取出插入的图片链接
'''

T = TypeVar('T', bound=ImageExtractResult)

class ImageExtractor:

    def extract(self, md_content:str) -> list[T]:
        raise NotImplementedError("This is extract function of ImageExtractor interface, it hasn't been implemented yet.")