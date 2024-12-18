# -*- coding: UTF-8 -*-
import importlib
import os
import re

from core.utils.file_utils import FileUtils
from core.utils.string_utils import StringUtils

'''
@Project  easy-post 
@File     package_scan_utils.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/17 11:45 
@Desc     Python包扫描工具类
'''


class PackageScanUtils:
    __reg_expression = r'class\s+([a-zA-Z_][a-zA-Z0-9_]*)(\([a-zA-Z0-9_, \.]*\))?'
    __property_pattern = r'@Component\(\s*singleton\s*=\s*(True|False)\)'

    _base_package: str = None

    def __init__(self, base_package: str):
        self._base_package = base_package

    """
    扫描指定包下被自定义注解@Component修饰的类
    """

    def scanComponentClass(self):
        project_basepath = StringUtils.get_project_basepath()
        project_basepath = StringUtils.replaceBackSlash(project_basepath)
        project_basepath = StringUtils.to_ends_with_back_slash(project_basepath)
        import_path_mappings = []
        for dirpath, dirnames, filenames in os.walk(self._base_package):
            for filename in filenames:
                if not filename.endswith(".py"):
                    continue
                if "__init__.py" == filename:
                    continue
                file_path = os.path.join(dirpath, filename)
                file_path = StringUtils.replaceBackSlash(file_path)
                relative_path = file_path.replace(project_basepath, "").replace(".py", "").replace("/", ".")
                class_name: str = None
                file_content = FileUtils.read_file_as_string(file_path)
                final_content = StringUtils.remove_comments(file_content)
                all_lines = final_content.split("\n")
                is_component = False
                line_index = 0
                for line in all_lines:
                    pattern = re.compile(self.__reg_expression)
                    matches = pattern.findall(line)
                    if matches is None or len(matches) <= 0:
                        line_index = line_index + 1
                        continue
                    class_name = matches[0][0]
                    is_singleton = True
                    if class_name is not None:
                        if line_index > 0:
                            prev_line = all_lines[line_index - 1]
                            prev_line = prev_line.strip("\n")
                            if prev_line is not None and len(prev_line) > 0:
                                if "@singleton" == prev_line or "@threadlocal" == prev_line:
                                    is_component = True
                                    if "@singleton" == prev_line:
                                        is_singleton = True
                                    else:
                                        is_singleton = False
                                else:
                                    is_component = False
                        line_index = line_index + 1
                        break
                    line_index = line_index + 1

                if class_name is None or not is_component:
                    continue
                import_path_mappings.append({"from": relative_path, "import": class_name, "singleton": is_singleton})
        return import_path_mappings

    # 动态导入模块
    def auto_import_modules(self, import_path_mappings: list):
        class_list = []
        for import_path_mapping in import_path_mappings:
            clazz_info = self.import_class(import_path_mapping)
            class_list.append(clazz_info)
        return class_list

    """
    动态导入模块中的类
    """

    def import_class(self, import_dict):
        module_path = import_dict['from']
        class_name = import_dict['import']
        is_singleton = import_dict['singleton'] if "singleton" in import_dict else True
        if is_singleton is None:
            is_singleton = True

        # 动态导入模块
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        return {"class": cls, "singleton": is_singleton}


if __name__ == '__main__':
    base_package = StringUtils.get_project_basepath()
    pageScanUtils = PackageScanUtils(base_package)
    import_path_mappings = pageScanUtils.scanComponentClass()
    mappings_json = StringUtils.to_json_str(import_path_mappings)
    print(mappings_json)
    class_list = pageScanUtils.auto_import_modules(import_path_mappings)
    for clazz in class_list:
        print(clazz)
        print(str(type(clazz)))
