from sqlalchemy.orm import Session
import datetime
from . import models, schemas


def get_customers(db: Session):
    return db.query(models.Customer).all()


# write CRUD operations for customers
def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(
        customerid=db.query(models.Customer).count() + 600,
        name=customer.name,
        email=customer.email,
        phone=customer.phone,
        address=customer.address,
        membersince=datetime.datetime.today(),
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def delete_customer(db: Session, customerid: int):
    db.query(models.Customer).filter(models.Customer.customerid == customerid).delete()
    db.commit()
    return {"message": "Customer deleted successfully."}


def customers_query(db: Session, query: str):
    if query == "1":
        return (
            db.query(models.Customer)
            .filter(models.Customer.membersince > datetime.datetime(2007, 7, 1))
            .all()
        )

    return db.query(models.Customer).order_by(models.Customer.membersince.desc()).all()


def get_customer(db: Session, customerid: int):
    return (
        db.query(models.Customer)
        .filter(models.Customer.customerid == customerid)
        .first()
    )
