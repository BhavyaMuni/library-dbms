from sqlalchemy.orm import Session
from . import models
import datetime


def drop_all_tables(db: Session):
    models.Base.metadata.drop_all(bind=db.get_bind())
    return {"message": "Tables dropped successfully."}


def populate_all_tables(db: Session):
    models.Base.metadata.create_all(bind=db.get_bind())
    categories = [
        (1, "Fantasy", "Fiction"),
        (2, "Science Fiction", "Fiction"),
        (3, "Action and Adventure", "Fiction"),
        (4, "Horror", "Fiction"),
        (5, "Thriller and Suspense", "Fiction"),
        (6, "Historical Fiction", "Fiction"),
        (7, "Romance", "Fiction/Non-fiction"),
        (8, "Memoir and Autobiography", "Non-fiction"),
        (9, "Biography", "Non-fiction"),
        (10, "Food and Drink", "Non-fiction"),
        (11, "Self-help", "Non-fiction"),
        (12, "History", "Non-fiction"),
        (13, "True Crime", "Non-fiction"),
        (14, "Travel", "Non-fiction"),
        (15, "Science and Technology", "Non-fiction"),
    ]

    customers = [
        (
            601,
            "Margaret Rouleau",
            "osaru@yahoo.ca",
            "(205) 857-3200",
            "23 Bradford St. Barrhead, AB T7N 0G4",
            datetime.datetime(2013, 7, 20, 12, 43, 2),
        ),
        (
            602,
            "Jenny Johnstone",
            "nachbaur@live.com",
            "(282) 878-7905",
            "771 Wintergreen Drive Grande-Anse, NB E8N 4G3",
            datetime.datetime(2017, 8, 24, 17, 53, 39),
        ),
        (
            603,
            "Alicia Leonard",
            "dimensio@att.net",
            "(587) 583-4405",
            "8 Windsor Road Sussex, NB E4E 9B0",
            datetime.datetime(2005, 10, 11, 21, 47, 26),
        ),
        (
            604,
            "Bobby Zhang",
            "jdhildeb@icloud.com",
            "(702) 911-6583",
            "8864 Washington Court Alder Point, NS B1Y 3Y9",
            datetime.datetime(2017, 10, 25, 4, 28, 17),
        ),
        (
            605,
            "John Doe",
            "jdoe@gmail.com",
            "(616) 704-7216",
            "9109 E. Garden Street Duncan, BC V9L 1C8",
            datetime.datetime(2014, 12, 15, 4, 12, 1),
        ),
    ]

    employees = [
        (
            501,
            "Rosalinda Levy",
            "thomasj@live.com",
            "(426) 851-3012",
            "6 S. Pheasant St. Clermont, QC G4A 7J0",
            "Librarian",
            datetime.datetime(2006, 5, 6, 21, 30, 31),
        ),
        (
            502,
            "June Mcknight",
            "goresky@outlook.com",
            "(846) 631-2076",
            "8210 Clay Ave. Fourchu, NS B2J 6G9",
            "Manager",
            datetime.datetime(2006, 10, 7, 4, 50, 17),
        ),
        (
            503,
            "Marc Cabrera",
            "konst@icloud.com",
            "(925) 709-5819",
            "9800 Tailwater Drive Ponoka, AB T4J 0A0",
            "Receptionist",
            datetime.datetime(2006, 9, 25, 20, 49, 14),
        ),
        (
            504,
            "Refugio Mcdaniel",
            "adhere@gmail.com",
            "(245) 415-5147",
            "38 Wrangler St. Leamington, ON N8H 8C2",
            "Librarian",
            datetime.datetime(2007, 11, 4, 23, 26, 25),
        ),
        (
            505,
            "Edgar Gonzalez",
            "lydia@hotmail.com",
            "(911) 658-5042",
            "111 Leatherwood Dr. Conception Bay, LB A1X 0M7",
            "Librarian",
            datetime.datetime(2008, 3, 22, 17, 40),
        ),
    ]
    books = [
        (
            100,
            "Journey to the End of the Night",
            "Louis-Ferdinand Celine",
            9,
            1992,
            10,
            10,
        ),
        (101, "Oedipus the King", "Sophocles", 6, 2012, 5, 5),
        (102, "Pride and Prejudice", "Jane Austen", 6, 2013, 10, 10),
        (103, "The Sound and the Fury", "William Faulkner", 7, 1987, 8, 8),
        (104, "Odyssey", "Homer", 10, 2006, 3, 0),
        (105, "Season of Migration to the North", "Tayeb Salih", 5, 2020, 9, 9),
        (106, "Moby Dick", "Herman Melville", 5, 2010, 10, 10),
        (107, "Medea", "Euripides", 9, 2018, 7, 7),
        (108, "Gypsy Ballads", "Federico Garcia Lorca", 2, 2003, 12, 12),
        (109, "To the Lighthouse", "Virginia Woolf", 9, 2006, 3, 3),
        (110, "Hamlet", "William Shakespeare", 7, 1989, 4, 4),
        (111, "Crime and Punishment", "Fyodor Dostoevsky", 10, 2012, 1, 0),
        (
            112,
            "One Hundred Years of Solitude",
            "Gabriel Garcia Marquez",
            10,
            2010,
            6,
            6,
        ),
        (113, "The recognition of Shakuntala", "Kalidasa", 8, 2013, 11, 11),
        (114, "The Stranger", "Albert Camus", 2, 1997, 9, 9),
    ]
    for i in categories:
        db.execute(models.Category.__table__.insert().values(i))
    db.flush()
    for i in books:
        db.execute(models.Book.__table__.insert().values(i))
    db.flush()
    for i in employees:
        db.execute(models.Employee.__table__.insert().values(i))
    db.flush()
    for i in customers:
        db.execute(models.Customer.__table__.insert().values(i))
    db.flush()
    db.commit()
    return {"message": "Tables populated successfully."}


# def get_categories(db: Session):
#     return db.query(models.Category).all()


# def get_category(db: Session, categoryid: int):
#     return (
#         db.query(models.Category)
#         .filter(models.Category.categoryid == categoryid)
#         .first()
#     )


# def get_employees(db: Session):
#     return db.query(models.Employee).all()


# def get_employee(db: Session, employeeid: int):
#     return (
#         db.query(models.Employee)
#         .filter(models.Employee.employeeid == employeeid)
#         .first()
#     )


# def create_employee(db: Session, employee: schemas.EmployeeCreate):
#     db_employee = models.Employee(
#         employeeid=db.query(models.Employee).count() + 100,
#         name=employee.name,
#         email=employee.email,
#         phone=employee.phone,
#         address=employee.address,
#         hiredate=employee.hiredate,
#     )
#     db.add(db_employee)
#     db.commit()
#     db.refresh(db_employee)
#     return db_employee
