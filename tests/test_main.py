from . import client


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    record = response.json()
    assert record["message"] == "Hello, world!"


def test_payer_crud():

    # params
    payer_name = "Darwin"

    # payload
    payload = {
        "name": payer_name,
    }

    # create object
    response = client.post("/payers", json=payload)
    assert response.status_code == 200
    record = response.json()
    payer_id = record["id"]
    assert record["name"] == payer_name

    # create twice (not ok)
    response = client.post("/payers", json=payload)
    assert response.status_code == 409
    error = response.json()
    assert "Duplicate entry" in error["detail"]

    # get object
    response = client.get(f"/payers/{payer_id}", json=payload)
    assert response.status_code == 200
    record = response.json()
    assert record["id"] == payer_id
    assert record["name"] == payer_name

    # delete object
    response = client.delete(f"/payers/{payer_id}", json=payload)
    assert response.status_code == 200
    record = response.json()
    assert record["id"] == payer_id
    assert record["name"] == payer_name

    # delete twice (not ok)
    response = client.delete(f"/payers/{payer_id}", json=payload)
    assert response.status_code == 404
    error = response.json()
    assert "Payer not found" in error["detail"]

    # get after delete (not ok)
    response = client.get(f"/payers/{payer_id}", json=payload)
    assert response.status_code == 404
    error = response.json()
    assert "Payer not found" in error["detail"]


def test_client_crud():

    # params
    payer_name = "Payer1"
    client_name = "Wallace"

    # payload
    payload = {
        "payer": {"name": payer_name},
        "name": client_name,
    }

    # create object
    response = client.post("/clients", json=payload)
    assert response.status_code == 200
    record = response.json()
    client_id = record["id"]
    assert record["name"] == client_name

    # create twice (not ok)
    response = client.post("/clients", json=payload)
    assert response.status_code == 409
    error = response.json()
    assert "Duplicate entry" in error["detail"]

    # get object
    response = client.get(f"/clients/{client_id}", json=payload)
    assert response.status_code == 200
    record = response.json()
    assert record["id"] == client_id
    assert record["name"] == client_name

    # delete object
    response = client.delete(f"/clients/{client_id}", json=payload)
    assert response.status_code == 200
    record = response.json()
    assert record["id"] == client_id
    assert record["name"] == client_name

    # delete twice (not ok)
    response = client.delete(f"/clients/{client_id}", json=payload)
    assert response.status_code == 404
    error = response.json()
    assert "Client not found" in error["detail"]

    # get after delete (not ok)
    response = client.get(f"/clients/{client_id}", json=payload)
    assert response.status_code == 404
    error = response.json()
    assert "Client not found" in error["detail"]


def test_task_crud():

    # params
    payer_name = "Payer1"
    client_name = "Client1"
    task_date = "2021-06-01"
    task_description = "I did a thing."
    task_hours = 2.5

    # payload
    payload = {
        "client": {"payer": {"name": payer_name}, "name": client_name,},
        "date": task_date,
        "description": task_description,
        "hours": task_hours,
    }

    # create object
    response = client.post("/tasks", json=payload)
    assert response.status_code == 200
    record = response.json()
    task_id = record["id"]
    assert record["date"] == task_date
    assert record["description"] == task_description
    assert record["hours"] == task_hours

    # create twice (not ok)
    response = client.post("/tasks", json=payload)
    assert response.status_code == 409
    error = response.json()
    assert "Duplicate entry" in error["detail"]

    # get object
    response = client.get(f"/tasks/{task_id}", json=payload)
    assert response.status_code == 200
    record = response.json()
    assert record["id"] == task_id
    assert record["date"] == task_date
    assert record["description"] == task_description
    assert record["hours"] == task_hours

    # delete object
    response = client.delete(f"/tasks/{task_id}", json=payload)
    assert response.status_code == 200
    record = response.json()
    assert record["id"] == task_id
    assert record["date"] == task_date
    assert record["description"] == task_description
    assert record["hours"] == task_hours

    # delete twice (not ok)
    response = client.delete(f"/tasks/{task_id}", json=payload)
    assert response.status_code == 404
    error = response.json()
    assert "Task not found" in error["detail"]

    # get after delete (not ok)
    response = client.get(f"/tasks/{task_id}", json=payload)
    assert response.status_code == 404
    error = response.json()
    assert "Task not found" in error["detail"]


def test_paycheck_crud():

    # params
    payer_name = "Payer1"
    paycheck_date = "2021-06-01"
    paycheck_amount = 2.5

    # payload
    payload = {
        "payer": {"name": payer_name},
        "date": paycheck_date,
        "amount": paycheck_amount,
    }

    # create object
    response = client.post("/paychecks", json=payload)
    assert response.status_code == 200
    record = response.json()
    paycheck_id = record["id"]
    assert record["date"] == paycheck_date
    assert record["amount"] == paycheck_amount

    # create twice (not ok)
    response = client.post("/paychecks", json=payload)
    assert response.status_code == 409
    error = response.json()
    assert "Duplicate entry" in error["detail"]

    # get object
    response = client.get(f"/paychecks/{paycheck_id}", json=payload)
    assert response.status_code == 200
    record = response.json()
    assert record["id"] == paycheck_id
    assert record["date"] == paycheck_date
    assert record["amount"] == paycheck_amount

    # delete object
    response = client.delete(f"/paychecks/{paycheck_id}", json=payload)
    assert response.status_code == 200
    record = response.json()
    assert record["id"] == paycheck_id
    assert record["date"] == paycheck_date
    assert record["amount"] == paycheck_amount

    # delete twice (not ok)
    response = client.delete(f"/paychecks/{paycheck_id}", json=payload)
    assert response.status_code == 404
    error = response.json()
    assert "Paycheck not found" in error["detail"]

    # get after delete (not ok)
    response = client.get(f"/paychecks/{paycheck_id}", json=payload)
    assert response.status_code == 404
    error = response.json()
    assert "Paycheck not found" in error["detail"]
