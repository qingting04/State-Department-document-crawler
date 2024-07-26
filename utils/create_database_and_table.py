import mysql.connector
from mysql.connector import Error


def create_database_and_table(dbname):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='ztw1016..',
            connect_timeout=20
        )

        if connection.is_connected():
            print("成功连接到 MySQL 服务器")
            cursor = connection.cursor()
            create_db_query = f"CREATE DATABASE IF NOT EXISTS {dbname}"
            cursor.execute(create_db_query)
            print(f"数据库 '{dbname}' 已创建或已经存在")
            cursor.execute(f"USE {dbname}")

            create_table_query = """
            CREATE TABLE IF NOT EXISTS gwy_wj1 (
                seq_id INT, 
                pub_url VARCHAR(255), 
                index_id VARCHAR(255),
                gov_theme VARCHAR(255), 
                pub_dept VARCHAR(255), 
                orig_date VARCHAR(255),
                doc_title VARCHAR(255), 
                pub_id VARCHAR(255), 
                pub_date VARCHAR(255), 
                doc_content LONGTEXT,
                PRIMARY KEY(seq_id)
            );
            CREATE TABLE IF NOT EXISTS gwy_wj2 (
                seq_id INT,
                pub_url VARCHAR(255),
                doc_title VARCHAR(255),
                pub_dept VARCHAR(255),
                pub_id VARCHAR(255),
                source VARCHAR(255),
                gov_theme VARCHAR(255),
                duc_types VARCHAR(255),
                orig_date VARCHAR(255),
                doc_content LONGTEXT,
                PRIMARY KEY(seq_id)
            );
            CREATE TABLE IF NOT EXISTS gwy_wj3 (
                seq_id INT,
                pub_url VARCHAR(255),
                doc_title VARCHAR(255),
                pub_date VARCHAR(255),
                source VARCHAR(255),
                doc_content LONGTEXT,
                PRIMARY KEY(seq_id)
            )
            """
            for result in cursor.execute(create_table_query, multi=True):
                pass
            print("表 'gwy_wj1、gwy_wj2、gwy_wj3' 已创建或已经存在")

    except Error as e:
        print(f"发生错误: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("数据库连接已关闭")