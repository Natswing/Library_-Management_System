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
    return_info_query=f"""SELECT 
    (CASE
        WHEN DaysDifference > 0 THEN (DaysDifference * 10 + rent_cost)
        ELSE rent_cost
    END) AS total_cost
    FROM
    (
        SELECT 
            user_name, 
            DATEDIFF(CURDATE(), due_date) AS DaysDifference,
            rent_cost 
        FROM
        (
            SELECT * 
            FROM trxn_log 
            WHERE user_name = '{username}'
            AND book_id = {book_id}
        ) AS a
    ) AS b;
    """
    result=mysql_obj.reader(return_info_query)
    total_cost=result[0]['total_cost']
    logger.info(f"{result}")
    
    return total_cost
