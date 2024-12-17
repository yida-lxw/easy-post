# -*- coding: UTF-8 -*-

'''
@Project  easy-post 
@File     component.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/17 11:13 
@Desc     自定义注解,用于标识当前类需要纳入IOC管理
'''


def Component(*args, **kwargs):
    def outer(cls):
        print(str(type(cls)))
        return cls

    return outer
