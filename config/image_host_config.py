# -*- coding: UTF-8 -*-
from image_host_type import ImageHostType

'''
@Project  easy-post 
@File     ImageHostConfig.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/16 15:35 
@Desc     图床配置类
'''


class ImageHostConfig:
    # 图床类型
    _image_host_type: ImageHostType = None

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def getImageHostType(self):
        return self._image_host_type
