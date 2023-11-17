from sqlalchemy.orm import Session

from . import models, schemas


def get_books(db: Session):
    return db.query(models.Book).all()


# write CRUD operations for books
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        id=db.query(models.Book).count() + 101,
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


def get_book(db: Session, bookid: int):
    return db.query(models.Book).filter(models.Book.bookid == bookid).first()


def get_categories(db: Session):
    return db.query(models.Category).all()


def get_category(db: Session, categoryid: int):
    return (
        db.query(models.Category)
        .filter(models.Category.categoryid == categoryid)
        .first()
    )
