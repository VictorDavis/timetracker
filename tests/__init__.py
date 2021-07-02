# bloody dependencies
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# internal imports
from timetracker.database import Base, SQLALCHEMY_DATABASE_URL, options
from timetracker.main import app, get_db

# ephemeral database
SQLALCHEMY_DATABASE_URL += "_UNITTESTS"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=options)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# override default db connection
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# test client
client = TestClient(app)

# static data
client.post("/payers", json={"name": "Payer1"})
client.post("/clients", json={"name": "Client1", "payer": {"name": "Payer1"}})
