# -*- coding: UTF-8 -*-

from injector import Injector

from core.inject.app_module import AppModule
from test.service.order.order_service import OrderService

'''
@Project  easy-post 
@File     inject_test.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/17 11:34 
@Desc     Python中IOC(依赖注入测试)
'''

injector = Injector([AppModule])
order_processor = injector.get(OrderService)

# 调用方法来处理订单
order_processor.process_order(order_id=3456, amount=150.0)
