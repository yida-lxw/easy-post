# -*- coding: UTF-8 -*-

from injector import Injector

from core.inject.app_module import AppModule
from image_upload.postimages.postimages_uploader import PostImagesUploader

'''
@Project  easy-post 
@File     postimages_upload_test.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/20 14:02 
@Desc     Type your description in one word at here.
'''

injector = Injector([AppModule])
postimages_uploader = injector.get(PostImagesUploader)
