# -*- coding: UTF-8 -*-

from injector import Module, singleton, threadlocal

from core.utils.package_scan_utils import PackageScanUtils
from core.utils.string_utils import StringUtils

'''
@Project  easy-post 
@File     app_module.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/17 11:23 
@Desc     Type your description in one word at here.
'''


class AppModule(Module):
    def configure(self, binder):
        base_package = StringUtils.get_project_basepath()
        pageScanUtils = PackageScanUtils(base_package)
        import_path_mappings = pageScanUtils.scanComponentClass()
        class_list = pageScanUtils.auto_import_modules(import_path_mappings)
        for clazz_info in class_list:
            clazz = clazz_info["class"]
            is_singleton = clazz_info["singleton"]
            if is_singleton:
                binder.bind(clazz, to=clazz, scope=singleton)
            else:
                binder.bind(clazz, to=clazz, scope=threadlocal)
