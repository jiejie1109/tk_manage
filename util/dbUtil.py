import sqlite3
from pathlib import Path
from util import dbpath
# db_filename=r'./db/video.db'
# 获取db文件下的路径
def get_db_connection(db_filename=dbpath.get_db_path()):
    # 获取数据库文件的路径
    db_path = Path(db_filename)
    # 尝试连接数据库
    try:
        conn = sqlite3.connect(str(db_path))
        print(f"试图打开的数据库文件路径: {db_path.resolve()}")  # 打印出实际的路径
        return conn
    except sqlite3.DatabaseError as e:
        print(f"无法打开数据库文件: {e}")
        return None


def close_db_connection(conn: sqlite3.Connection):
    if conn:
        conn.close()
        print("数据库连接已关闭")


# 创建user表
def create_user_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
        """
    )
    conn.commit()
    print("表 'user' 创建成功。")


# 创建资源类别表
def create_resource_Type_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS resource_type (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resourceTypeName varchar(20) DEFAULT NULL,
            resourceTypeDesc varchar(1000) DEFAULT NULL
        );
        """
    )
    conn.commit()
    print("表 'resource_Type' 创建成功。")


# 创建资源表
def create_resource_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS resource (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resourceName varchar(20) DEFAULT NULL,
            author varchar(20) DEFAULT NULL,
            sex varchar(20) DEFAULT NULL,
            price float DEFAULT NULL,
            resourceTypeId integer DEFAULT NULL,
            resourceDesc varchar(1000) DEFAULT NULL,
            FOREIGN KEY (resourceTypeId) REFERENCES resource_type(id)
        );
        """
    )
    conn.commit()
    print("表 'resource' 创建成功。")


# 检查表是否存在
def check_table_exists(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name=?;
        """, (table_name,)
    )
    result = cursor.fetchone()
    return result is not None


# 查看表列表
def list_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cursor.fetchall()


# 查看表的内容
def query_db(conn, table):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    return cursor.fetchall()


if __name__ == '__main__':
    conn = get_db_connection()
    print(query_db(conn, 'resource'))
