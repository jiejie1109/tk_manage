# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/30 9:59
# @File    : resourceModel.py
# @Software: PyCharm
class Resources:
    id = None
    resourceName = None
    author = None
    sex = "男"
    price = None
    resourceTypeId = -1
    resourceDesc = None

    def __init__(self, resourceName, author, resourceTypeId):
        self.resourceName = resourceName
        self.author = author
        self.resourceTypeId = resourceTypeId

    @staticmethod
    def my_constructor(resourceName, author, sex, price, resourceTypeId, resourceDesc):
        obj = Resources(resourceName, author, resourceTypeId)
        obj.sex = sex
        obj.price = price
        obj.resourceDesc = resourceDesc
        return obj

    @staticmethod
    def my_constructor2(id, resourceName, author, sex, price, resourceTypeId, resourceDesc):
        obj = Resources(resourceName, author, resourceTypeId)
        obj.id = id
        obj.sex = sex
        obj.price = price
        obj.resourceDesc = resourceDesc
        return obj
