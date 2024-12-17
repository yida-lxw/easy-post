# -*- coding: UTF-8 -*-
from injector import inject

from core.anno.component import Component
from test.service.payment.payment_service import PaymentService
from test.service.shipping.shipping_service import ShippingService

'''
@Project  easy-post 
@File     order_service.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/17 11:32 
@Desc     Type your description in one word at here.
'''


@Component
class OrderService:
    @inject
    def __init__(self, payment_service: PaymentService, shipping_service: ShippingService):
        self.payment_service = payment_service
        self.shipping_service = shipping_service

    def process_order(self, order_id, amount):
        self.payment_service.process_payment(amount)
        self.shipping_service.ship_order(order_id)
