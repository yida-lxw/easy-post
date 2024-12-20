# -*- coding: UTF-8 -*-
from injector import singleton

from config.image_host_config_reader import ImageHostConfigReader
from config.image_host_type import ImageHostType
from core.utils.file_utils import FileUtils
from core.utils.string_utils import StringUtils

'''
@Project  easy-post 
@File     post_images_host_config_reader.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/20 18:00 
@Desc     PostImages图床配置读取器
'''


@singleton
class PostImagesHostConfigReader(ImageHostConfigReader):

    def __init__(self):
        self._image_host_type = ImageHostType.POSTIMAGES

    def load_config(self) -> dict:
        config_sub_folder_name = self._image_host_type["host_name"]
        project_basepath = StringUtils.get_project_basepath()
        project_basepath = StringUtils.replaceBackSlash(project_basepath)
        project_basepath = StringUtils.to_ends_with_back_slash(project_basepath)
        config_file_path = (project_basepath + "config/" + config_sub_folder_name + "/" + \
                            config_sub_folder_name + "-host-config.json")
        config_file_content = FileUtils.read_file_as_string(config_file_path)
        if StringUtils.is_empty(config_file_content):
            print(f"the config file:{config_file_path} is empty. please check it out.")
            return {}
        return StringUtils.json_to_dict(config_file_content)
