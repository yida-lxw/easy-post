# -*- coding: UTF-8 -*-
from typing import TypeVar

from config.image_host_config import ImageHostConfig

'''
@Project  easy-post 
@File     image_uploader.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/16 15:05 
@Desc     图片上传接口
'''

C = TypeVar('C', bound=ImageHostConfig)


class ImageUploader:
    _image_host_config: C = None

    def upload(self, image_file_path: str) -> str:
        raise NotImplementedError("This is upload function of ImageUploader interface, it hasn't been implemented yet.")

    def setImageHostConfig(self, image_host_config: C):
        self._image_host_config = image_host_config
