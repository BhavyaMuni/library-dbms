from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import crud, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
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
def read_book(db: Session = Depends(get_db)):
    book = crud.get_books(db)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
