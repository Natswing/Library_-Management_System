from database.reader import *
from schema.schema import *
from utility.utils import *

mysql_obj=mysql_connection()

def return_logic(return_info):
    book_name=return_info['book_name']
    username=return_info['username']
    book_id_query=f"select book_id from book_log where name='{book_name}' "
    result=mysql_obj.reader(book_id_query)
    book_id=result[0]["book_id"]
    
