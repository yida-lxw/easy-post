# -*- coding: UTF-8 -*-
from core.anno.component import Component

'''
@Project  easy-post 
@File     shipping_service.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/17 11:22 
@Desc     Type your description in one word at here.
'''


@Component
class ShippingService:
    def ship_order(self, order_id):
        print(f'Shipping order {order_id} through ShippingService.')
