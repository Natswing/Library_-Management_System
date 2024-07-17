from schema.schema import *
from database.reader import *
from utility.utils import *

mysql_obj=mysql_connection()


def book_avalibility_checker(book_name):

    query = f""" select * from book_log where name = '{book_name}' """
    result = mysql_obj.reader(query)

    if len(result)==0:
        return {"Message": "Book name is incorrect."}
    else:
        logger.info(f"{result}")
        book_id = result[0]['book_id']
        logger.info(f"{book_id}")
        if book_id:
            result=get_book_stock(book_id)
        return result  


def get_book_stock(book_id):
    query= f""" select no_of_books from inventory where book_id = {book_id} 
             """
    result = mysql_obj.reader(query)
    result=result[0]["no_of_books"]

    return result



