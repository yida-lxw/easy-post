# -*- coding: utf-8 -*-

import os


class CommandExecuteUtils:
    @staticmethod
    def execute_command(command: str):
        os.system("chcp 65001")
        result = os.system(command)
        return result
