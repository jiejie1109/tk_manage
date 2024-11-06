# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/10/29 14:35
# @File    : resourceDao.py
# @Software: PyCharm
from entity.resourceModel import Resources
from util import dbUtil, dbpath


def countByTypeOd(typeId):
    """
    根据类别id查询资源数量
    :param typeId:
    :return:
    """
    conn = None
    try:
        conn = dbUtil.get_db_connection(dbpath.get_db_path())
        cursor = conn.cursor()
        cursor.execute(f"select count(*) as total from resource where resourceTypeId={typeId}")
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return None
    finally:
        dbUtil.close_db_connection(conn)


def add(resource: Resources):
    """
    资源添加
    :param resource: 资源实体
    :return: 执行的条数
    """
    conn = None
    try:
        conn = dbUtil.get_db_connection(dbpath.get_db_path())
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO resource(resourceName, author, sex, price, resourceTypeId, resourceDesc) VALUES (?, ?, ?, ?, ?, ?);
            """,
            (resource.resourceName, resource.author, resource.sex, resource.price, resource.resourceTypeId,
             resource.resourceDesc)
        )
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        print(e)
    finally:
        dbUtil.close_db_connection(conn)


def list_re(s_rename: Resources):
    """
    更具条件查询信息
    :param s_rename:
    :return:
    """
    conn = None
    try:
        conn = dbUtil.get_db_connection(dbpath.get_db_path())
        cursor = conn.cursor()
        sql = f"SELECT re.id AS id,resourceName,author,resourceTypeName,sex,price,resourceDesc FROM resource re,resource_type re_t WHERE re.resourceTypeId = re_t.id"
        if s_rename is not None:
            if s_rename.resourceName.strip() != "":
                sql += " and re.resourceName like '%" + s_rename.resourceName + "%' "
            if s_rename.author.strip() != "":
                sql += " and re.author like '%" + s_rename.author + "%' "
            if s_rename.resourceTypeId != -1:
                sql += " and re.resourceTypeId like '%" + str(s_rename.resourceTypeId) + "%' "
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return None
    finally:
        dbUtil.close_db_connection(conn)


def update(resource: Resources):
    """
    资源类别修改
    :param resource: 资源实体
    :return: 执行的条数
    """
    conn = None
    try:
        conn = dbUtil.get_db_connection(dbpath.get_db_path())
        cursor = conn.cursor()
        cursor.execute(
            f"update resource set resourceName='{resource.resourceName}',author='{resource.author}',sex='{resource.sex}',price='{resource.price}',resourceTypeId={resource.resourceTypeId},resourceDesc='{resource.resourceDesc}' where id={resource.id}")
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        print(e)
        return 0
    finally:
        dbUtil.close_db_connection(conn)

def delete(id: int):
    """
    资源删除
    :param id: id
    :return: 执行的条数
    """
    conn = None
    try:
        conn = dbUtil.get_db_connection(dbpath.get_db_path())
        cursor = conn.cursor()
        cursor.execute(f"delete from resource where id = {id}")
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        print(e)
        return 0
    finally:
        dbUtil.close_db_connection(conn)