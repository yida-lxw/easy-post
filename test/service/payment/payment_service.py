# -*- coding: UTF-8 -*-
from core.anno.component import Component

'''
@Project  easy-post 
@File     payment_service.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/17 11:21 
@Desc     Type your description in one word at here.
'''


@Component
class PaymentService:
    def process_payment(self, amount):
        print(f'Processing payment of ${amount} through PaymentService.')
