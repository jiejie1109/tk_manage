# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/29 10:49
# @File    : dbpath.py
# @Software: PyCharm
import os


# 在util包下db下获取video的路径

def get_db_path():
    return os.path.join(os.path.dirname(__file__), 'db', 'video.db')


if __name__ == '__main__':
    print(get_db_path())
