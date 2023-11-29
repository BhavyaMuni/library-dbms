from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from db import crud, models, schemas
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
    allow_methods=["GET", "POST", "DELETE"],
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
    books = crud.get_books(db)
    if books is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return books


@app.post("/api/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.create_book(db=db, book=book)
    return db_book


@app.delete("/api/books/{bookid}")
def delete_book(bookid: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db=db, bookid=bookid)
    return db_book


@app.get("/api/books/query-{qid}", response_model=list[schemas.Book])
def run_query(qid: str, db: Session = Depends(get_db)):
    books = crud.books_query(db=db, query=qid)
    if books is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return books
