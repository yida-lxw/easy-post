# -*- coding: UTF-8 -*-
from typing import TypeVar

from config.image_host_config import ImageHostConfig
from config.image_host_type import ImageHostType

'''
@Project  easy-post 
@File     image_host_config_reader.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/20 18:01 
@Desc     图床配置读取器
'''

T = TypeVar('T', bound=ImageHostConfig)

class ImageHostConfigReader:
    _image_host_type: ImageHostType = None

    def load_config(self) -> T:
        raise NotImplementedError(
            "This is load_config function of ImageHostConfigReader interface, it hasn't been implemented yet.")
