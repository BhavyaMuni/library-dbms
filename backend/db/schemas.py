from pydantic import BaseModel
from typing import Optional
from datetime import date


class BookBase(BaseModel):
    title: str
    author: str
    publishedyear: int
    totalstock: int
    availablestock: int


class Book(BookBase):
    bookid: int

    class Config:
        orm_mode = True


class BookCreate(BookBase):
    categoryid: int


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class Category(CategoryBase):
    categoryid: int

    class Config:
        orm_mode = True


class EmployeeBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    role: str


class Employee(EmployeeBase):
    employeeid: int
    hiredate: date

    class Config:
        orm_mode = True


class EmployeeCreate(EmployeeBase):
    pass


class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str


class Customer(CustomerBase):
    customerid: int
    membersince: date

    class Config:
        orm_mode = True


class CustomerCreate(CustomerBase):
    pass


class TransactionBase(BaseModel):
    bookid: int
    customerid: int
    employeeid: int
    checkoutdate: date
    duedate: date
    returndate: Optional[date] = None
    latefee: Optional[int] = None


class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True
