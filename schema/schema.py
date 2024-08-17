from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class SignupBody(BaseModel):
    username:str
    password:str
    address:Optional[str]
    phone_no:str 
    first_name:str
    last_name:Optional[str]
    
class LoginBody(BaseModel):
    username:str
    password:str

class BookInfo(BaseModel):
    name:str

class BookIssue(BaseModel):
    username:str
    book_name:str

class ReturnBook(BaseModel):
    username:str
    book_name:str  

class NewBookLog(BaseModel):
    book_name:str
    book_department:str
    book_cost:int
    rent_cost:int
    author:Optional[str]=None
    no_of_pages:Optional[int]=None
    library_id:int

class NewBookInventoryData(BaseModel):
    book_name:str
    no_of_books:int
