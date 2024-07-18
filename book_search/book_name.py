from utility.utils import *

mysql_obj=mysql_connection()
def find_book_name_from_tbl(keyword):
    query = f""" select * from book_log where name like '%{keyword}%'
"""
    result = mysql_obj.reader(query)

    if len(result)==0:
        return {"Message": "Book Not found"}
    else:
        logger.info(f"{result}")
        column_list=["name","department",'author',"rent_cost"]
        final_result=[]
        for i in range (len(result)):
            d={}
            for key in result[i]:
                if key in column_list:
                    d[key]=result[i][key]
            final_result.append(d)
    
        logger.info(f"{final_result}")
        return final_result   