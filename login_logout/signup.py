from fastapi import HTTPException
from database.reader import *
from utility.utils import *
from loguru import logger

mysql_obj=mysql_connection()
# mysql_obj.connection
def user_signup_logic(user_input):
    username=user_input['username']
    password=user_input['password']
    result = login_checker(username,password,mysql_obj)
    logger.info(f"{len(result)}")
    if len(result)!=0:
        raise HTTPException(status_code=406, detail="User already exists.")
        # return {"Message": "Username already exists."}
    else:
        logger.info("Inserting data into table.")
        construct_insert_statement(user_input)
        return {"Message": "Signup Succesful"}

def construct_insert_statement(user_input):
    user_input["joining_date"]="now()"
    column = ",".join(user_input.keys())
    logger.info(f"Column data: {column}")
    values=""
    for i in range(len(user_input)-1):
        values+="%s"+","
    values=values[:-1]+",now()"
    logger.info(f"%s data: {values}")
    t=tuple(user_input.values())[:-1]
    logger.info(f"Values data: {t}")
    insert_query=f"insert into user_tbl ({column}) values ({values})"
    cursor=mysql_obj.connection.cursor()
    logger.info(f"{insert_query}")

    cursor.execute(insert_query,t)
    mysql_obj.connection.commit()
    cursor.close()
