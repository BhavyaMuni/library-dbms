from sqlalchemy.orm import Session

from . import models


def get_books(db: Session):
    return db.query(models.Book).all()


def get_book(db: Session, bookid: int):
    return db.query(models.Book).filter(models.Book.bookid == bookid).first()


def get_categories(db: Session):
    return db.query(models.Category).all()
