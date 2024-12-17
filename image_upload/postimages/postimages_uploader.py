# -*- coding: UTF-8 -*-
import os

from config.post_images_host_config import PostImagesHostConfig
from core.utils.file_utils import FileUtils
from core.utils.string_utils import StringUtils
from image_upload.image_uploader import ImageUploader
from image_upload.postimages.postimages_service import PostImagesService

'''
@Project  easy-post 
@File     PostImageUploader.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/17 9:32 
@Desc     PostImages图床图片上传服务
'''


class PostImagesUploader(ImageUploader):
    _postimages_service: PostImagesService
    # 存放cookie文件的目录名称
    _cookies_folder_name = "postimages"

    def login(self) -> dict:
        email = self._image_host_config.username
        password = self._image_host_config.password
        # TODO 这里后续需要考虑使用单例注入, 避免过多创建实例对象
        postimages_service = PostImagesService(email, password)
        cookies = postimages_service.login()
        if cookies is not None and len(cookies) > 0:
            cookies_json = StringUtils.to_json_str(cookies, beautify=True)
            project_basepath = StringUtils.get_project_basepath()
            project_basepath = StringUtils.replaceBackSlash(project_basepath)
            project_basepath = StringUtils.to_ends_with_back_slash(project_basepath)
            cookie_file_path = project_basepath + "config/" + self._cookies_folder_name + "/cookies.txt"
            FileUtils.write_string_to_file(cookies_json, cookie_file_path)
        return cookies

    def upload(self, image_file_path: str) -> str:
        project_basepath = StringUtils.get_project_basepath()
        project_basepath = StringUtils.replaceBackSlash(project_basepath)
        project_basepath = StringUtils.to_ends_with_back_slash(project_basepath)
        cookie_file_path = project_basepath + "config/" + self._cookies_folder_name + "/cookies.txt"
        # 用于标识是否需要重新登录
        required_relogin = False
        # 若当前图床的本地cookie文件不存在,则需要先执行登录操作
        if not os.path.exists(cookie_file_path):
            self.login()
            required_relogin = True
        else:
            cookies_json = FileUtils.read_file_as_string(cookie_file_path)
            if cookies_json is None or len(cookies_json) <= 0:
                self.login()
                required_relogin = True
            else:
                cookies_dict = StringUtils.json_to_dict(cookies_json)
        image_host_config: PostImagesHostConfig = type(PostImagesHostConfig)(self._image_host_config)
        email = self._image_host_config.username
        password = self._image_host_config.password
        gallery_name = image_host_config.gallery_name
        # TODO 这里后续需要考虑使用单例注入, 避免过多创建实例对象
        if required_relogin:
            postimages_service = PostImagesService(email, password)
        else:
            postimages_service = PostImagesService(email, password, cookies=cookies_dict)
        postimages_service.set_working_gallery(gallery_name)
        image_urls = postimages_service.upload_image(image_file_path)
        if image_urls:
            print(f"Upload image:[{image_file_path}] successfully, the response data was:{image_urls}")
            return image_urls
        else:
            raise RuntimeError(f"Image:[{image_file_path}] upload failed.")
