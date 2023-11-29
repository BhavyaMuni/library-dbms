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


def get_categories(db: Session):
    return db.query(models.Category).all()


def get_category(db: Session, categoryid: int):
    return (
        db.query(models.Category)
        .filter(models.Category.categoryid == categoryid)
        .first()
    )


def get_employees(db: Session):
    return db.query(models.Employee).all()


def get_employee(db: Session, employeeid: int):
    return (
        db.query(models.Employee)
        .filter(models.Employee.employeeid == employeeid)
        .first()
    )


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        employeeid=db.query(models.Employee).count() + 100,
        name=employee.name,
        email=employee.email,
        phone=employee.phone,
        address=employee.address,
        hiredate=employee.hiredate,
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
