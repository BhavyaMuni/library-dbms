from sqlalchemy.orm import Session

from . import models, schemas

import datetime


def get_employees(db: Session):
    return db.query(models.Employee).all()


# write CRUD operations for employees
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        employeeid=db.query(models.Employee).count() + 500,
        name=employee.name,
        email=employee.email,
        phone=employee.phone,
        address=employee.address,
        hiredate=datetime.datetime.today(),
        role=employee.role,
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, employeeid: int):
    db.query(models.Employee).filter(models.Employee.employeeid == employeeid).delete()
    db.commit()
    return {"message": "Employee deleted successfully."}


def employees_query(db: Session, query: str):
    if query == "1":
        return (
            db.query(models.Employee)
            .filter(models.Employee.hiredate > datetime.datetime(2007, 7, 1))
            .all()
        )

    return (
        db.query(models.Employee)
        .filter(models.Employee.role == "Librarian")
        .order_by(models.Employee.hiredate.desc())
        .all()
    )


def get_employee(db: Session, employeeid: int):
    return (
        db.query(models.Employee)
        .filter(models.Employee.employeeid == employeeid)
        .first()
    )
