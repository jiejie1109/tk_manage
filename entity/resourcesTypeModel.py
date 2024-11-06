# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/29 9:46
# @File    : resourcesTypeModel.py
# @Software: PyCharm
class ResourcesType:
    id = None
    resourceTypeName = None
    resourceTypeDesc = None

    def __init__(self, resourceTypeName, resourceTypeDesc):
        self.resourceTypeName = resourceTypeName
        self.resourceTypeDesc = resourceTypeDesc

    # 静态方法重载init 加入id
    @staticmethod
    def my_constructor(id, resourceTypeName, resourceTypeDesc):
        obj = ResourcesType(resourceTypeName, resourceTypeDesc)
        obj.id = id
        return obj
