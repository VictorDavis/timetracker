# bloody dependencies
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint

# internal imports
from .database import Base


class Common:
    @declared_attr
    def __table_args__(cls):
        table_name = cls.__tablename__
        table_keys = cls.__tablekeys__
        return (UniqueConstraint(*table_keys, name=f"uq_{table_name}"),)

    # common fields
    id = Column(Integer, primary_key=True)


class Payer(Common, Base):
    __tablename__ = "payers"
    __tablekeys__ = ["name"]

    name = Column(String(16), nullable=False)


class Client(Common, Base):
    __tablename__ = "clients"
    __tablekeys__ = ["name"]

    payer_id = Column(ForeignKey(Payer.id), index=True, nullable=False)
    name = Column(String(16), nullable=False)

    payer = relationship(Payer, backref="clients")


class Paycheck(Common, Base):
    __tablename__ = "paychecks"
    __tablekeys__ = ["payer_id", "date"]

    payer_id = Column(ForeignKey(Payer.id), index=True, nullable=False)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)

    payer = relationship(Payer, backref="paychecks")


class Task(Common, Base):
    __tablename__ = "tasks"
    __tablekeys__ = ["client_id", "date"]

    client_id = Column(ForeignKey(Client.id), index=True, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String(1024), nullable=False)
    hours = Column(Float, nullable=False)
    paycheck_id = Column(ForeignKey(Paycheck.id), index=True)

    client = relationship(Client, backref="tasks")
    paycheck = relationship(Paycheck, backref="tasks")
