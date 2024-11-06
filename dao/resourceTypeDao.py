# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/29 9:57
# @File    : resourceTypeDao.py
# @Software: PyCharm
from entity.resourcesTypeModel import ResourcesType
from util import dbUtil
from util import dbpath


def add(resourceType: ResourcesType):
    """
    资源类别添加
    :param resourceType: 资源类别实体
    :return: 执行的条数
    """
    conn = None
    try:
        conn = dbUtil.get_db_connection(dbpath.get_db_path())
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO resource_type(resourceTypeName, resourceTypeDesc) VALUES (?, ?);
            """,
            (resourceType.resourceTypeName, resourceType.resourceTypeDesc)
        )
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        print(e)
    finally:
        dbUtil.close_db_connection(conn)


# 搜索资源类别
def list(s_resourceTypeName: str):
    """
    资源类别列表
    :param s_resourceTypeName: 资源类别名称
    :return: 资源类别列表
    """
    conn = None
    try:
        conn = dbUtil.get_db_connection(dbpath.get_db_path())
        cursor = conn.cursor()
        sql = "select * from resource_type where 1=1"
        if s_resourceTypeName.strip() != "":
            sql += " and resourceTypeName like '%" + s_resourceTypeName + "%' "
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return None
    finally:
        dbUtil.close_db_connection(conn)


def update(resourceType: ResourcesType):
    """
    资源类别修改
    :param resourceType: 资源类别实体
    :return: 执行的条数
    """
    conn = None
    try:
        conn = dbUtil.get_db_connection(dbpath.get_db_path())
        cursor = conn.cursor()
        cursor.execute(
            f"update resource_type set resourceTypeName='{resourceType.resourceTypeName}',resourceTypeDesc='{resourceType.resourceTypeDesc}' where id={resourceType.id}")
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        print(e)
        return 0
    finally:
        dbUtil.close_db_connection(conn)


def delete(id: int):
    """
    资源类别删除
    :param id: id
    :return: 执行的条数
    """
    conn = None
    try:
        conn = dbUtil.get_db_connection(dbpath.get_db_path())
        cursor = conn.cursor()
        cursor.execute(f"delete from resource_type where id = {id}")
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        print(e)
        return 0
    finally:
        dbUtil.close_db_connection(conn)


if __name__ == '__main__':
    print(list("111"))
