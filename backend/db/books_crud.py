from operator import or_
from sqlalchemy.orm import Session

from . import models, schemas


def get_books(db: Session):
    return db.query(models.Book).all()


# write CRUD operations for books
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        bookid=db.query(models.Book).count() + 100,
        title=book.title,
        author=book.author,
        publishedyear=book.publishedyear,
        totalstock=book.totalstock,
        availablestock=book.availablestock,
        categoryid=book.categoryid,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, bookid: int):
    db.query(models.Book).filter(models.Book.bookid == bookid).delete()
    db.commit()
    return {"message": "Book deleted successfully."}


def books_query(db: Session, query: str):
    if query == "1":
        return db.query(models.Book).filter(models.Book.publishedyear > 2011).all()

    return (
        db.query(models.Book)
        .filter(or_(models.Book.categoryid == 6, models.Book.categoryid == 2))
        .order_by(models.Book.publishedyear.desc())
        .all()
    )


def get_book(db: Session, bookid: int):
    return db.query(models.Book).filter(models.Book.bookid == bookid).first()
