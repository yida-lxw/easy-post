# -*- coding: utf-8 -*-

import os

from core.utils.os_utils import OSUtils

'''
@Project  easy-post 
@File     os_utils.py
@IDE      PyCharm
@Author   yida
@Email    949226420@qq.com
@Date     2024.12.10 17:05
@Desc     执行命令行下的命令的工具类
'''
class CommandExecuteUtils:
    @staticmethod
    def execute_command(command: str):
        os_type = OSUtils.get_os_type()
        if "windows" == os_type:
            os.system("chcp 65001")
        else:
            os.system("export LANG=en_US.UTF-8")
        # os.system(command)
        data = os.popen(command).readlines()
        return data
