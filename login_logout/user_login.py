from database.reader import *
from utility.utils import *
import datetime
from loguru import logger

mysql_obj=mysql_connection()

# mysql_obj.connection
def user_login_logic(user_input):
    username=user_input['username']
    password=user_input['password']
    result = login_checker(username,password,mysql_obj)
    if len(result)==0:
        return {"Message": "Invalid username or password"}
    else:
        return {"Message": "Login Succesful"}


def login_status(username,status,mysql_obj):
    connection=mysql_obj.connection
    logger.info(f"{connection}")
    current_time=datetime.datetime.now()
    formatted = current_time.strftime("%Y-%m-%d %H:%M:%S")
    cursor=connection.cursor()
    insert_query =f"""insert into user (username,login_time,status) 
    values('{username}',now(),'{status}')"""
    logger.info(insert_query)
    cursor.execute(insert_query)
    connection.commit()
    cursor.close()



