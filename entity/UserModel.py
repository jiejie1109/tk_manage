# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/24 15:35
# @File    : UserModel.py
# @Software: PyCharm
# 用户实体类
class User:
    # 编号 主键
    id = None
    # 用户名
    username = None
    # 密码
    password = None
    # 新密码
    newPassword = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def my_constructor(username, password, newPassword):
        obj = User(username, password)
        obj.newPassword = newPassword
        return obj
