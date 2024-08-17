from database.reader import *
from schema.schema import *
from utility.utils import *

mysql_obj=mysql_connection()


def new_book_update_logic(new_book_info):
    book_name=new_book_info["book_name"]
    book_department=new_book_info["book_department"]
    book_cost=new_book_info["book_cost"]
    rent_cost=new_book_info["rent_cost"]
    author=new_book_info["author"]
    no_of_pages=new_book_info["no_of_pages"]
    library_id=new_book_info["library_id"]
    if author is not None and no_of_pages is not None:
        book_log_insert_query=f"""Insert into book_log (name,department,book_cost,   
        rent_cost,author,no_of_pages,library_id)
        values('{book_name}','{book_department}',{book_cost},{rent_cost},'{author}',
        {no_of_pages},{library_id})
        """
        mysql_obj.writer(book_log_insert_query)
    else:
        book_log_insert_query=f"""Insert into book_log (name,department,book_cost,
        rent_cost,library_id)
        values('{book_name}','{book_department}',{book_cost},{rent_cost},{library_id})
        """
        mysql_obj.writer(book_log_insert_query)
    
    return {"Message" : "New Book added Successfully."}



