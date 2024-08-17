from database.reader import *
from schema.schema import *
from utility.utils import *

mysql_obj=mysql_connection()

def new_book_inventory_update_logic(new_book_inventory_info):
    book_name=new_book_inventory_info["book_name"]
    no_of_books=new_book_inventory_info["no_of_books"]
    book_id_query=f""" select book_id from book_log where name='{book_name}' """
    result=mysql_obj.reader(book_id_query)
    book_id=result[0]["book_id"]
    update_query=f""" insert into inventory (book_id,no_of_books)
    values ({book_id},{no_of_books}) """
    result=mysql_obj.writer(update_query)
    return {"message":"Inventory updated successfully."}
