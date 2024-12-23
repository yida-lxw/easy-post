# -*- coding: UTF-8 -*-

from injector import Injector

from config.postimages.postimages_host_config import PostImagesHostConfig
from config.postimages.postimages_host_config_reader import PostImagesHostConfigReader
from core.inject.app_module import AppModule
from image_upload.postimages.postimages_uploader import PostImagesUploader

'''
@Project  easy-post 
@File     postimages_upload_test.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/20 14:02 
@Desc     postimages图床图片上传单元测试
'''

injector = Injector([AppModule])
imageHostConfigReader = injector.get(PostImagesHostConfigReader)
image_host_config = imageHostConfigReader.load_config()
postimages_host_config: PostImagesHostConfig = injector.get(PostImagesHostConfig)
postimages_host_config.email = image_host_config.username
postimages_host_config.password = image_host_config.password
postimages_host_config.gallery_name = image_host_config.gallery_name
postimages_uploader = injector.get(PostImagesUploader)
postimages_uploader.login()
image_file_path = "F:/chrome_downloads/mudan.jpg"
postimages_uploader.upload(image_file_path)
