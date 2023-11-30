import datetime
from sqlalchemy.orm import Session

from . import models, schemas


def get_transactions(db: Session):
    return db.query(models.Transaction).all()


# write CRUD operations for transactions
def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(
        transactionid=db.query(models.Transaction).count() + 1,
        bookid=transaction.bookid,
        customerid=transaction.customerid,
        employeeid=transaction.employeeid,
        checkoutdate=transaction.checkoutdate,
        duedate=transaction.duedate,
        returndate=transaction.returndate,
        latefee=transaction.latefee,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def delete_transaction(db: Session, transactionid: int):
    db.query(models.Transaction).filter(
        models.Transaction.transactionid == transactionid
    ).delete()
    db.commit()
    return {"message": "Transaction deleted successfully."}


def transactions_query(db: Session, query: str):
    if query == "1":
        return (
            db.query(models.Transaction)
            .filter(models.Transaction.checkoutdate > datetime.datetime(2013, 7, 1))
            .order_by(models.Transaction.checkoutdate.desc())
            .all()
        )

    return (
        db.query(models.Transaction)
        .filter(models.Transaction.employeeid == 501)
        .order_by(models.Transaction.checkoutdate.desc())
        .all()
    )


def get_transaction(db: Session, transactionid: int):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.transactionid == transactionid)
        .first()
    )
