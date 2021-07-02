# bloody dependencies
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

# internal imports
from . import models, schemas

# UTIL: add or 409
def add_or_409(db, object):
    try:
        db.add(object)
        db.commit()
        db.refresh(object)
    except IntegrityError as error:
        detail = error.orig.args[1]
        raise HTTPException(status_code=409, detail=detail)


# UTIL: delete or 409
def delete_or_409(db, object):
    try:
        db.delete(object)
        db.commit()
    except IntegrityError as error:
        detail = error.orig.args[1]
        raise HTTPException(status_code=409, detail=detail)


def list_payers(db: Session):
    payers = db.query(models.Payer).all()
    return payers


def get_payer(db: Session, id: int):
    payers = db.query(models.Payer)
    payer = payers.get(id)
    if not payer:
        raise HTTPException(status_code=404, detail="Payer not found!")
    return payer


def find_payer(db: Session, name: str):
    payers = db.query(models.Payer)
    payers = payers.filter(models.Payer.name == name)
    payer = payers.one_or_none()
    if not payer:
        raise HTTPException(status_code=404, detail="Payer not found!")
    return payer


def create_payer(db: Session, data):

    # create object
    object = models.Payer(**data.dict())

    # add object to db
    add_or_409(db, object)

    # return added object
    return object


def delete_payer(db: Session, id: int):

    # get object
    payer = get_payer(db, id)

    # delete object
    delete_or_409(db, payer)

    # return deleted object
    return payer


def list_clients(db: Session):
    clients = db.query(models.Client).all()
    return clients


def get_client(db: Session, id: int):
    clients = db.query(models.Client)
    client = clients.get(id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found!")
    return client


def find_client(db: Session, name: str):
    clients = db.query(models.Client)
    clients = clients.filter(models.Client.name == name)
    client = clients.one_or_none()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found!")
    return client


def create_client(db: Session, data):

    # get object's dependent objects
    data.payer = find_payer(db, data.payer.name)

    # create object
    object = models.Client(**data.dict())

    # add object to db
    add_or_409(db, object)

    # return added object
    return object


def delete_client(db: Session, id: int):

    # get object
    client = get_client(db, id)

    # delete object
    delete_or_409(db, client)

    # return deleted object
    return client


def list_tasks(db: Session):
    tasks = db.query(models.Task).all()
    return tasks


def get_task(db: Session, id: int):
    tasks = db.query(models.Task)
    task = tasks.get(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found!")
    return task


def create_task(db: Session, data):

    # get object's dependent objects
    data.client = find_client(db, data.client.name)

    # create object
    object = models.Task(**data.dict())

    # add object to db
    add_or_409(db, object)

    # return added object
    return object


def delete_task(db: Session, id: int):

    # get object
    task = get_task(db, id)

    # delete object
    delete_or_409(db, task)

    # return deleted object
    return task


def list_paychecks(db: Session):
    paychecks = db.query(models.Paycheck).all()
    return paychecks


def get_paycheck(db: Session, id: int):
    paychecks = db.query(models.Paycheck)
    paycheck = paychecks.get(id)
    if not paycheck:
        raise HTTPException(status_code=404, detail="Paycheck not found!")
    return paycheck


def create_paycheck(db: Session, data):

    # get object's dependent objects
    data.payer = find_payer(db, data.payer.name)

    # create object
    object = models.Paycheck(**data.dict())

    # add object to db
    add_or_409(db, object)

    # return added object
    return object


def delete_paycheck(db: Session, id: int):

    # get object
    paycheck = get_paycheck(db, id)

    # delete object
    delete_or_409(db, paycheck)

    # return deleted object
    return paycheck
