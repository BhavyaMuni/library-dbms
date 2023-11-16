from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class Book(Base):
    __tablename__ = "books"
    bookid = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    author = Column(String)
    publishedyear = Column(Integer)
    totalstock = Column(Integer)
    availablestock = Column(Integer)
    categoryid = Column(Integer, ForeignKey("categories.id"))


class Category(Base):
    __tablename__ = "categories"
    categoryid = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)


class Employee(Base):
    __tablename__ = "employees"
    employeeid = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    address = Column(String)
    hiredate = Column(Date)


class Customer(Base):
    __tablename__ = "customers"

    customerid = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    address = Column(String)
    membersince = Column(Date)


class Transaction(Base):
    __tablename__ = "transactions"

    transactionid = Column(Integer, primary_key=True, index=True)
    bookid = Column(Integer, ForeignKey("books.id"))
    customerid = Column(Integer, ForeignKey("customers.id"))
    employeeid = Column(Integer, ForeignKey("employees.id"))
    checkoutdate = Column(Date)
    duedate = Column(Date)
    returndate = Column(Date)
    latefee = Column(Integer)
