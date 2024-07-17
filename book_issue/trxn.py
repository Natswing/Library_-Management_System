from database.reader import *
from schema.schema import *
from utility.utils import *

mysql_obj=mysql_connection()


def trxn_logic(trxn_info):
    book_name=trxn_info['book_name']
    username=trxn_info['username']
    query=f"""select book_id , rent_cost,library_id from book_log where name='{book_name}'"""
    result=mysql_obj.reader(query)
    book_id=result[0]['book_id']
    data=booking_validator(username,book_id)
    logger.info(f"{data}")
    if not data:
        return{"Message":"User alredy has a booking"}
    rent_cost =result[0]['rent_cost']
    library_id=result[0]['library_id']
    insert_query=f"""insert into trxn_log (user_name,library_id,book_id,rent_cost,
    issue_date,due_date) values ('{username}',{library_id},{book_id},{rent_cost},
    cast(now() as date),DATE_ADD(cast(now() as date),INTERVAL 30 DAY))"""
    mysql_obj.writer(insert_query)

    select_query=f"""select no_of_books from
    inventory where book_id={book_id}"""
    result=mysql_obj.reader(select_query)
    logger.info(f"{type(result)}")
    result=result[0]["no_of_books"]
    update_query=f"""update inventory set no_of_books = ({result}-1) where book_id={book_id}"""
    mysql_obj.writer(update_query)
    return {"Message":"Booking Successful"}

def booking_validator(username,book_id)->bool:
    check_query=f""" select user_name from trxn_log where user_name = '{username}' and 
    book_id = {book_id}"""
    result=mysql_obj.reader(check_query)
    if len(result) != 0:
        return False
    else :
        return True




    





