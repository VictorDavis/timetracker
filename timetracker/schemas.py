# bloody dependencies
from datetime import date
from enum import Enum
from pydantic import BaseModel
from typing import Optional


class Common(BaseModel):
    class Config:
        orm_mode = True


class Payer(Common):
    name: str


class Client(Common):
    payer: Payer
    name: str


class Task(Common):
    client: Client
    date: date
    description: Optional[str]
    hours: float


class Paycheck(Common):
    payer: Payer
    date: date
    amount: float
