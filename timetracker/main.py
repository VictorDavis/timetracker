# bloody dependencies
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

# internal imports
from . import crud, schemas
from .database import SessionLocal, engine, Base

# TODO: setup/teardown tables in separate step
Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.post("/clients")
async def create_client(client: schemas.Client, db: Session = Depends(get_db)):
    client_created = crud.create_client(db, client)
    return client_created


@app.get("/clients")
async def list_clients(db: Session = Depends(get_db)):
    all_clients = crud.list_clients(db)
    return all_clients


@app.get("/clients/{client_id}")
async def get_client(client_id: int, db: Session = Depends(get_db)):
    client_retrieved = crud.get_client(db, client_id)
    return client_retrieved


@app.delete("/clients/{client_id}")
async def delete_client(client_id: int, db: Session = Depends(get_db)):
    client_deleted = crud.delete_client(db, client_id)
    return client_deleted


@app.post("/payers")
async def create_payer(payer: schemas.Payer, db: Session = Depends(get_db)):
    payer_created = crud.create_payer(db, payer)
    return payer_created


@app.get("/payers")
async def list_payers(db: Session = Depends(get_db)):
    all_payers = crud.list_payers(db)
    return all_payers


@app.get("/payers/{payer_id}")
async def get_payer(payer_id: int, db: Session = Depends(get_db)):
    payer_retrieved = crud.get_payer(db, payer_id)
    return payer_retrieved


@app.delete("/payers/{payer_id}")
async def delete_payer(payer_id: int, db: Session = Depends(get_db)):
    payer_deleted = crud.delete_payer(db, payer_id)
    return payer_deleted


@app.post("/paychecks")
async def create_paycheck(paycheck: schemas.Paycheck, db: Session = Depends(get_db)):
    paycheck_created = crud.create_paycheck(db, paycheck)
    return paycheck_created


@app.get("/paychecks/{paycheck_id}")
async def get_paycheck(paycheck_id: int, db: Session = Depends(get_db)):
    paycheck_retrieved = crud.get_paycheck(db, paycheck_id)
    return paycheck_retrieved


@app.delete("/paychecks/{paycheck_id}")
async def delete_paycheck(paycheck_id: int, db: Session = Depends(get_db)):
    paycheck_deleted = crud.delete_paycheck(db, paycheck_id)
    return paycheck_deleted


@app.post("/tasks")
async def create_task(task: schemas.Task, db: Session = Depends(get_db)):
    task_created = crud.create_task(db, task)
    return task_created


@app.get("/tasks/{task_id}")
async def get_task(task_id: int, db: Session = Depends(get_db)):
    task_retrieved = crud.get_task(db, task_id)
    return task_retrieved


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task_deleted = crud.delete_task(db, task_id)
    return task_deleted
