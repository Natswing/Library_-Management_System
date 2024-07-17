from database.reader import *
from loguru import logger

def mysql_connection():
    mysql_obj = MySqlConnection(host="localhost",user='root',password='54321',
                            database='lib_management_sys')
    return mysql_obj

def login_checker(username,password,mysql_obj):
    connection= mysql_obj.connection
    logger.info(mysql_obj.connection)
    logger.info(f"{connection}")
    cursor=connection.cursor()
    select_query =f"select * from user_tbl where username = '{username}' and password ='{password}'"
    result=cursor.execute(select_query)
    rows=cursor.fetchall()
    return rows

