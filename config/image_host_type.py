# -*- coding: UTF-8 -*-
from enum import Enum

'''
@Project  easy-post 
@File     image_host_type.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/16 15:50 
@Desc     图床类型枚举
'''


class ImageHostType(Enum):
    POSTIMAGES = {"code": 1, "host_name": "postimages"}
    SM_MS = {"code": 2, "host_name": "smms"}
