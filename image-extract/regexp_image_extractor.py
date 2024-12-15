# -*- coding: utf-8 -*-

import re
from image_extractor import ImageExtractor, T
from image_extract_result import ImageExtractResult
'''
@Project  easy-post
@File     regexp_image_extractor.py
@IDE      PyCharm
@Author   yida
@Email    949226420@qq.com
@Date     2024.12.15 14:58
@Desc     使用正则表达式从MD文档中提取出插入的图片链接
'''

class RegExpImageExtractor(ImageExtractor):
    _pattern = '(!\\[(.*?)\\]\\((.*?)\\))'

    """
    传入md文档的字符串文本，返回提取到的插入图片链接
    """
    def extract(self, md_content: str) -> list[T]:
        matches = re.findall(self._pattern, md_content)
        result_list = []
        for match in matches:
            image_label_full_text = match[0]
            image_name = match[1]
            image_file_path = match[2]
            imageExtractResult = ImageExtractResult(image_label_full_text, image_name, image_file_path)
            result_list.append(imageExtractResult)
        return result_list