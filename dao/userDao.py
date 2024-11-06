# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/24 15:39
# @File    : userDao.py
# @Software: PyCharm
# 数据访问对象
from entity.UserModel import User
from util.dbUtil import get_db_connection, close_db_connection, check_table_exists, create_user_table, \
    create_resource_table, create_resource_Type_table
from util import dbpath
# 记录当前登录用户
current_user: User = None


def login(user: User):
    """
    用户登录判断
    :param user: 用户实体
    :return: 登录成功 返回用户信息实体 登录失败返回None
    """
    # 初始化 conn 变量
    conn = None
    try:
        # 检查表是否存在，如果不存在则创建
        conn = get_db_connection(dbpath.get_db_path())
        print(f"获取链接{conn}")
        if not check_table_exists(conn=conn, table_name="user"):
            create_user_table(conn=conn)
            #     插入数据
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                ("admin", "123")
            )
            # 持久化
            conn.commit()
            print("数据初始化成功。")

        # 在登录时候初始化其他表
        # 类别表
        create_resource_Type_table(conn)
        # 资源表
        create_resource_table(conn)

        cursor = conn.cursor()
        # 使用参数化查询来防止SQL注入
        cursor.execute(
            "SELECT * FROM user WHERE username = ? AND password = ?",
            (user.username, user.password)
        )
        return cursor.fetchone()
    except Exception as e:
        print(e)
    finally:
        if conn:  # 确保 conn 不为 None 时才调用 close
            close_db_connection(conn)
def modifyPassword(user: User):
    """
    修改密码
    :param user: 修改密码
    :return: 执行的条数
    """
    conn = None
    try:
        conn = get_db_connection(dbpath.get_db_path())
        cursor = conn.cursor()
        cursor.execute(
            f"update user set password='{user.newPassword}' where username='{user.username}'")
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        print(e)
        return 0
    finally:
        close_db_connection(conn)


if __name__ == '__main__':
    print(login(User("123", "123")))
