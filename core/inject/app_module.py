# -*- coding: UTF-8 -*-
from injector import Module, singleton

from test.service.payment.payment_service import PaymentService
from test.service.shipping.shipping_service import ShippingService

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
        binder.bind(PaymentService, to=PaymentService, scope=singleton)
        binder.bind(ShippingService, to=ShippingService, scope=singleton)
