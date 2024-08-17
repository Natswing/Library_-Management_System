from typing import Union
from loguru import logger
from fastapi import FastAPI
from schema.schema import *
from login_logout.signup import *
from login_logout.user_login import *
from book_search.book_name import *
from book_search.book_avl import *
from book_issue.trxn import *
from book_return.book_return import *
from new_book_update.new_book_log import *
from new_book_update.inventory_update import *


app = FastAPI()

@app.post("/user_signup")
def user_signup(user_data:SignupBody):
    user_data=user_data.model_dump()
    logger.info(type(user_data))
    result=user_signup_logic(user_data)
    return result


@app.post("/user_login")
def user_login(user_input:LoginBody):
    user_input=user_input.model_dump()
    logger.info(type(user_input))
    # call user_login logic here
    result=user_login_logic(user_input)
    return result


@app.post("/find_book_name")
def find_book_name(keyword:str):
    result = find_book_name_from_tbl(keyword)
    logger.info(f"{result}")
    return result


@app.post("/book_availabilty_search")
def book_availability_search(book_avl:BookInfo):
    book_avl=book_avl.model_dump()["name"]
    logger.info(f"{book_avl}")
    result=book_avalibility_checker(book_avl)
    return result


@app.post("/issue_book")
def issue_book(trxn_info:BookIssue):
    trxn_info=trxn_info.model_dump()
    logger.info(f"{trxn_info}")
    result=trxn_logic(trxn_info)
    return result

@app.post("/return_book")
def return_book(return_info:ReturnBook):
    return_info=return_info.model_dump()
    logger.info(f"{return_info}")
    result=return_logic(return_info)
    return {"Message" : f"Total rent to be paid is {result}"}


@app.post("/book_log_update")
def book_log_update(new_book_info:NewBookLog):
    new_book_info=new_book_info.model_dump()
    logger.info(f"{new_book_info}")
    result=new_book_update_logic(new_book_info)
    return result

@app.post("/new_book_inventory_update")
def new_book_inventory_update(new_book_inventory_info:NewBookInventoryData):
    new_book_inventory_info=new_book_inventory_info.model_dump()
    logger.info(f"{new_book_inventory_info}")
    result=new_book_update_logic(new_book_inventory_info)
    return result

@app.post("/inventory_update")
def inventory_update(inventory_update_info:NewBookInventoryData):
    inventory_update_info=inventory_update_info.model_dump()
    logger.info(f"{inventory_update_info}")
    result=new_book_inventory_update_logic(inventory_update_info)
    return result


   
