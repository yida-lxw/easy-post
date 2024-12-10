# -*- coding: utf-8 -*-

import os
import shutil

from core.utils.string_utils import StringUtils

'''
@Project  easy-post 
@File     file_utils.py
@IDE      PyCharm
@Author   yida
@Email    949226420@qq.com
@Date     2024.12.10 13:52
@Desc     文件操作工具类
'''
class FileUtils:
    @staticmethod
    def copy_file(src_file, dest_file):
        try:
            shutil.copyfile(src_file, dest_file)
            return True
        except:
            return False

    @staticmethod
    def get_files_in(directory):
        file_list = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list

    @staticmethod
    # 删除指定文件
    def deleteFileIfExists(file_path):
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                return True
            except:
                return False
        else:
            return False

    @staticmethod
    # 删除指定目录
    def deleteFolderIfExists(folder_path):
        if os.path.exists(folder_path):
            shutil.rmtree(path=folder_path, ignore_errors=True)

    """
    从给定文件路径中提取文件名(不包含文件后缀名)
    """

    @staticmethod
    def get_filename_without_suffix(file_path):
        file_name = os.path.basename(file_path)
        file_name = os.path.splitext(file_name)[0]
        return file_name

    """
    从给定文件名称中提取文件后缀名(不包含文件后缀名)
    """

    @staticmethod
    def get_suffix(file_name: str, include_dot: bool = True):
        index = file_name.find(".")
        if index == -1:
            return ""
        if not include_dot:
            index = index + 1
        suffix = file_name[index: len(file_name)]
        return suffix

    """
    从文件名称中提取不包含后缀名的文件名
    """

    @staticmethod
    def get_file_name_without_suffix(file_name: str):
        index = file_name.find(".")
        if index == -1:
            return file_name
        target_file_name = file_name[0: index]
        return target_file_name

    # 复制目录及其所有子文件和子目录
    @staticmethod
    def copyFolder(source_folder_path, target_folder_path):
        shutil.copytree(source_folder_path, target_folder_path)

    # 文件重命名
    @staticmethod
    def rename_file(orignal_file_path, new_file_name):
        if StringUtils.is_empty(orignal_file_path) or StringUtils.is_empty(new_file_name):
            return False
        parent_dir = os.path.dirname(orignal_file_path)
        parent_dir = StringUtils.replaceBackSlash(parent_dir)
        parent_dir = StringUtils.to_ends_with_back_slash(parent_dir)
        file_name = os.path.basename(orignal_file_path)
        new_suffix = FileUtils.get_suffix(new_file_name, include_dot=True)
        if StringUtils.is_not_empty(new_suffix):
            new_suffix = new_suffix.lower()
            target_new_file_name = FileUtils.get_file_name_without_suffix(new_file_name)
            final_new_file_name = target_new_file_name + new_suffix
        else:
            final_new_file_name = new_file_name
        # 若新文件名与原始文件名相同,则不需要执行文件重命名操作
        if StringUtils.equals(file_name, final_new_file_name):
            return False
        new_file_abspath = os.path.join(parent_dir, final_new_file_name)
        try:
            os.rename(orignal_file_path, new_file_abspath)
            return True
        except Exception as e:
            return False
