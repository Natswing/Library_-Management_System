from loguru import logger
import mysql.connector

class MySqlConnection:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password=password
        self.database=database
        self.connection=mysql.connector.connect(host=self.host,
                                    user=self.user,
                                    password =self.password,
                                    database = self.database)
    def reader(self,query):
        logger.info(f"Running query {query}")
        cursor=self.connection.cursor()
        result=cursor.execute(query)
        # rows=cursor.fetchall()
        results = [dict(zip([column[0] for column in cursor.description], row)) 
                    for row in cursor.fetchall()]
        return results
    
    def writer(self,query):
        logger.info(f'Running query {query}')
        cursor=self.connection.cursor()
        result=cursor.execute(query)
        self.connection.commit()
        cursor.close()
