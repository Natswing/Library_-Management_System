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