# -*- coding: UTF-8 -*-
from injector import singleton

from config.image_host_config import ImageHostConfig
from config.image_host_type import ImageHostType

'''
@Project  easy-post 
@File     PostImagesHostConfig.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/16 17:55 
@Desc     PostImages图床配置类
'''


@singleton
class PostImagesHostConfig(ImageHostConfig):
    def __init__(self, email: str = None, password: str = None, gallery_name: str = None):
        self.username = email
        self.password = password
        self.email = email
        self.gallery_name = gallery_name
        self._image_host_type = ImageHostType.POSTIMAGES
