from sqlalchemy import Column, ForeignKey, Identity
from sqlalchemy.dialects.oracle import NUMBER, VARCHAR2, DATE
from .database import Base


class Book(Base):
    __tablename__ = "books"
    bookid = Column(
        NUMBER,
        primary_key=True,
    )
    title = Column(
        VARCHAR2(32),
        unique=True,
    )
    author = Column(VARCHAR2(32))
    categoryid = Column(NUMBER, ForeignKey("categories.categoryid"))
    publishedyear = Column(NUMBER)
    totalstock = Column(NUMBER)
    availablestock = Column(NUMBER)


class Category(Base):
    __tablename__ = "categories"
    categoryid = Column(NUMBER, Identity(start=1), primary_key=True)
    name = Column(VARCHAR2(32))
    description = Column(VARCHAR2(32))


class Employee(Base):
    __tablename__ = "employees"
    employeeid = Column(
        NUMBER,
        primary_key=True,
    )
    name = Column(VARCHAR2(32), unique=True)
    email = Column(
        VARCHAR2(32),
        unique=True,
    )
    phone = Column(VARCHAR2(32))
    address = Column(VARCHAR2(64))
    role = Column(VARCHAR2(32))
    hiredate = Column(DATE)


class Customer(Base):
    __tablename__ = "customers"

    customerid = Column(
        NUMBER,
        primary_key=True,
    )
    name = Column(VARCHAR2(32), unique=True)
    email = Column(
        VARCHAR2(32),
        unique=True,
    )
    phone = Column(VARCHAR2(32))
    address = Column(VARCHAR2(64))
    membersince = Column(DATE)


class Transaction(Base):
    __tablename__ = "transactions"

    transactionid = Column(
        NUMBER,
        primary_key=True,
    )
    bookid = Column(NUMBER, ForeignKey("books.bookid"))
    customerid = Column(NUMBER, ForeignKey("customers.customerid"))
    employeeid = Column(NUMBER, ForeignKey("employees.employeeid"))
    checkoutdate = Column(DATE)
    duedate = Column(DATE)
    returndate = Column(DATE)
    latefee = Column(NUMBER)
