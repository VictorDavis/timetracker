# bloody dependencies
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# globals
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/timetracker"

options = {}
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=options)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
