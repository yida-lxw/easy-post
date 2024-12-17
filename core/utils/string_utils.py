# -*- coding: utf-8 -*-

import json
import os
import random
import re

'''
@Project  easy-post 
@File     string_utils.py
@IDE      PyCharm
@Author   yida
@Email    949226420@qq.com
@Date     2024.12.10 14:20
@Desc     字符串操作工具类
'''
class StringUtils:
    """
    判断给定字符串是否为空
    """

    @staticmethod
    def is_empty(orignal_str: str):
        return orignal_str is None or len(orignal_str) == 0

    """
    判断给定字符串是否不为空
    """

    @staticmethod
    def is_not_empty(orignal_str: str):
        return not StringUtils.is_empty(orignal_str)

    # 查找指定字符在original_string字符串中最后一次出现的位置
    @staticmethod
    def lastIndexOf(original_string: str, substr: str) -> int:
        if original_string is None or substr is None:
            raise ValueError("string and substr could not be None.")
        elif not (isinstance(original_string, str) and isinstance(substr, str)):
            raise TypeError("string and substr must be str type.")
        elif not (len(original_string) > 0 and 0 < len(substr) <= len(original_string)):
            raise TypeError("string and substr value must be non empty, "
                            "and string's length must more over than substr's length.")
        last_index = -1
        idx = 0
        while True:
            try:
                index = original_string.index(substr, idx)
                last_index = index
                idx = index + len(substr)
            except ValueError:
                return last_index

    """
    判断两个字符串是否相等(比较时区分大小写)
    """
    @staticmethod
    def equals(str1: str, str2: str):
        if str1 is None and str2 is None:
            return True
        if str1 == "" and str2 == "":
            return True
        if str1 is None and str2 is not None:
            return False
        if str1 is not None and str2 is None:
            return False
        return str1 == str2

    """
    判断两个字符串是否不相等(比较时区分大小写)
    """

    @staticmethod
    def not_equals(str1: str, str2: str):
        return not StringUtils.equals(str1, str2)

    """
    判断两个字符串是否相等(比较时忽略字符串的大小写)
    """

    @staticmethod
    def equals_ignore_case(str1: str, str2: str):
        if str1 is None and str2 is None:
            return True
        if str1 == "" and str2 == "":
            return True
        if str1 is None and str2 is not None:
            return False
        if str1 is not None and str2 is None:
            return False
        return str1.lower() == str2.lower()

    """
    判断两个字符串是否不相等(比较时忽略字符串的大小写)
    """

    @staticmethod
    def not_equals_ignore_case(str1: str, str2: str):
        return not StringUtils.equals_ignore_case(str1, str2)

    """
    文件路径中的反斜杠\转换为正斜杠/
    """

    @staticmethod
    def replaceBackSlash(file_path: str):
        if StringUtils.is_empty(file_path):
            return file_path
        file_path = file_path.replace("\\", "/")
        return file_path

    """
    若文件路径不是以正斜杠/结尾, 则转化为以正斜杠/结尾
    """

    @staticmethod
    def to_ends_with_back_slash(file_path: str):
        if "\\" in file_path:
            file_path = StringUtils.replaceBackSlash(file_path)
        if file_path.endswith("/"):
            return file_path
        file_path = file_path + "/"
        return file_path

    """
    剔除掉末尾的正斜杠或反斜杠
    """

    @staticmethod
    def trim_last_slash(file_path: str):
        if "\\" in file_path:
            file_path = StringUtils.replaceBackSlash(file_path)
        if not file_path.endswith("/"):
            return file_path
        file_path = file_path[0: len(file_path) - 1]
        return file_path

    """
    数字添加前导字符,使其最终长度达到指定的total_len大小
    """
    @staticmethod
    def left_pad_zero(num: int, total_len: int = 5):
        return str(num).zfill(total_len)

    # 获取当前项目的根路径
    @staticmethod
    def get_project_basepath():
        current_dir = os.getcwd()
        while not os.path.exists(os.path.join(current_dir, 'requirements.txt')):
            current_dir = os.path.dirname(current_dir)
        return current_dir

    # 生成[start, end]区间内的随机数(双闭区间)
    @staticmethod
    def random_num(start, end):
        return random.randint(start, end)

    # 将Python对象格式化为JSON字符串
    @staticmethod
    def to_json_str(obj, beautify: bool = False):
        if beautify:
            return json.dumps(obj, indent=4)
        else:
            return json.dumps(obj)

    # JSON字符串转成dict类型
    @staticmethod
    def json_to_dict(json_string: str) -> dict:
        dict_data = json.loads(json_string)
        return dict_data

    # 删除py文件中的注释
    @staticmethod
    def remove_comments(file_content):
        # First, find and store string assignments
        protected_strings = {}
        counter = 0

        def protect_string_assignments(match):
            nonlocal counter
            var_name, string_content = match.groups()
            key = f'PROTECTED_STRING_{counter}'
            protected_strings[key] = match.group(0)
            counter += 1
            return key

        # Protect strings that are part of assignments
        protected_content = re.sub(
            r'([a-zA-Z_][a-zA-Z0-9_]*\s*=\s*)("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')',
            protect_string_assignments,
            file_content
        )

        # Remove docstring comments (triple-quoted strings not part of assignments)
        cleaned_content = re.sub(
            r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'',
            '',
            protected_content
        )

        # Remove single-line comments and empty lines
        lines = []
        for line in cleaned_content.split('\n'):
            # Remove inline comments
            line = re.sub(r'#.*$', '', line)
            if line.strip():
                lines.append(line)

        # Restore protected strings
        final_content = '\n'.join(lines)
        for key, value in protected_strings.items():
            final_content = final_content.replace(key, value)
        return final_content
