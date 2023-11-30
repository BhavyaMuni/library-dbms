from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db import (
    crud,
    models,
    schemas,
    books_crud,
    customers_crud,
    employees_crud,
    transactions_crud,
)
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="https://library-dbms-frontend.vercel.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/healthchecker")
def healthchecker():
    return {"status": "success", "message": "Integrate FastAPI Framework with Next.js"}


@app.get("/api")
def read_root():
    return {"Hello": "World"}


@app.get("/api/books", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    books = books_crud.get_books(db)
    if books is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return books


@app.post("/api/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = books_crud.create_book(db=db, book=book)
    return db_book


@app.get("/api/books/{bookid}", response_model=schemas.Book)
def read_book(bookid: int, db: Session = Depends(get_db)):
    db_book = books_crud.get_book(db=db, bookid=bookid)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.delete("/api/books/{bookid}")
def delete_book(bookid: int, db: Session = Depends(get_db)):
    db_book = books_crud.delete_book(db=db, bookid=bookid)
    return db_book


@app.get("/api/books/query-{qid}", response_model=list[schemas.Book])
def run_query_books(qid: str, db: Session = Depends(get_db)):
    books = books_crud.books_query(db=db, query=qid)
    if books is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return books


@app.get("/api/customers", response_model=list[schemas.Customer])
def read_customers(db: Session = Depends(get_db)):
    customers = customers_crud.get_customers(db)
    if customers is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customers


@app.post("/api/customers", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = customers_crud.create_customer(db=db, customer=customer)
    return db_customer


@app.delete("/api/customers/{customerid}")
def delete_customer(customerid: int, db: Session = Depends(get_db)):
    db_customer = customers_crud.delete_customer(db=db, customerid=customerid)
    return db_customer


@app.get("/api/customers/query-{qid}", response_model=list[schemas.Customer])
def run_query_customers(qid: str, db: Session = Depends(get_db)):
    customers = customers_crud.customers_query(db=db, query=qid)
    if customers is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customers


@app.get("/api/employees", response_model=list[schemas.Employee])
def read_employees(db: Session = Depends(get_db)):
    employees = employees_crud.get_employees(db)
    if employees is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return employees


@app.post("/api/employees", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = employees_crud.create_employee(db=db, employee=employee)
    return db_employee


@app.delete("/api/employees/{employeeid}")
def delete_employee(employeeid: int, db: Session = Depends(get_db)):
    db_employee = employees_crud.delete_employee(db=db, employeeid=employeeid)
    return db_employee


@app.get("/api/employees/query-{qid}", response_model=list[schemas.Employee])
def run_query_employees(qid: str, db: Session = Depends(get_db)):
    employees = employees_crud.employees_query(db=db, query=qid)
    if employees is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employees


@app.get("/api/transactions", response_model=list[schemas.Transaction])
def read_transactions(db: Session = Depends(get_db)):
    transactions = transactions_crud.get_transactions(db)
    print(transactions)
    if transactions is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transactions


@app.post("/api/transactions", response_model=schemas.Transaction)
def create_transaction(
    transaction: schemas.TransactionCreate, db: Session = Depends(get_db)
):
    db_transaction = transactions_crud.create_transaction(
        db=db, transaction=transaction
    )
    return db_transaction


@app.delete("/api/transactions/{transactionid}")
def delete_transaction(transactionid: int, db: Session = Depends(get_db)):
    db_transaction = transactions_crud.delete_transaction(
        db=db, transactionid=transactionid
    )
    return db_transaction


@app.get("/api/transactions/query-{qid}", response_model=list[schemas.Transaction])
def run_query_transactions(qid: str, db: Session = Depends(get_db)):
    transactions = transactions_crud.transactions_query(db=db, query=qid)
    if transactions is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transactions


@app.get("/api/populate-all")
def populate_tables(db: Session = Depends(get_db)):
    books = crud.populate_all_tables(db=db)
    return books


@app.delete("/api/drop-all")
def drop_tables(db: Session = Depends(get_db)):
    books = crud.drop_all_tables(db=db)
    return books
