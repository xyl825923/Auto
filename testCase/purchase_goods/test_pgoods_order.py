# -*- coding: UTF-8 -*-
"""
@Project: Auto
@Author : yuling xiao
@Date : 2023/6/29 20:07
@File : test_pgoods_order.py
@Describe:
    购货订单
"""
from common.keys import ApiKeys
from configs.read_conf import read_conf


class TestPurGoodsOrderApi:
    # 购货订单新增
    def test_addPgOrder(self):
        api = ApiKeys()
        data = {
            "id": -1,
            "buId": "129663929532192",
            "contactName": "1",
            "date": "2023-06-29",
            "deliveryDate": "2023-06-29",
            "billNo": "GHDD20230629001",
            "transType": "150501",
            "entries": [{
                "invId": "129663929532135",
                "invNumber": "SP001",
                "invName": "测试1",
                "invSpec": "",
                "skuId": -1,
                "skuName": "",
                "unitId": -1,
                "mainUnit": "",
                "baseQty": "100",
                "baseUnit": "",
                "qty": "100",
                "price": "520.10",
                "taxPrice": "520.10",
                "discountRate": "0",
                "deduction": "0.00",
                "amount": "52010.00",
                "goodsDiscountRate": "0.00",
                "description": "",
                "locationId": "1291101929135756",
                "locationName": "默认仓库",
                "srcOrderEntryId": "",
                "srcOrderId": "",
                "srcOrderNo": "",
                "customcol1": "",
                "customcol2": "",
                "customcol3": "",
                "customcol4": "",
                "customcol5": "",
                "isGift": 0,
                "shelfNames": "",
                "taxRate": "0",
                "tax": "0.00",
                "taxAmount": "52010.00",
                "snapshotQty": "0"
            }],
            "totalQty": "100",
            "totalAmount": "52010.00",
            "description": "",
            "disRate": "0.00",
            "disAmount": "0",
            "amount": "52010.00",
            "splitPackTotal": "",
            "totalTax": "0.00",
            "totalTaxAmount": "52010.00",
            "deliveryMethod": 0
        }
        # headers = read_conf('headers', 'cookies')
        # print(headers)
        #
        res = api.do_post(path='invPo.do?action=checkInvPo', data=data, headers=read_conf('headers', 'yssession'))
        print(res.text)
