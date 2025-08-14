import requests

# 🔐 Token & Base URL config
BASE_URL = "http://localhost:8000/api/employees/"
TOKEN = "f1633fd99190402551fd2b9bd750020908a188bb"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Token {TOKEN}"
}

# ✅ Test: Add Employee with All Valid Fields
def test_add_employee():
    data = {
        "name": "Ravi Kumar",
        "email": "ravi202@example.com",
        "phone": "9876543210",
        "address": "123 Street, Delhi",
        "date_of_joining": "2023-01-15",
        "department_id": 1  # 👈 Department ID, not name
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201


# ✅ Test: Get Employee by ID (static test)
def test_get_employee():
    response = requests.get(BASE_URL + "1/", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert "name" in data

# ❌ FIX: This test had wrong field 'position' which is not in your model
def test_add_employee_missing_name():
    data = {
        "email": "test202@example.com",
        "phone": "9999999999",
        "address": "Test Nagar",
        "date_of_joining": "2024-05-10",
        "department": "HR"
        # 'name' missing — intentional
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=data)
    print(response.text)
    assert response.status_code == 400

# ✅ Test: Get a non-existent employee
def test_get_non_existing_employee():
    response = requests.get(BASE_URL + "999/", headers=HEADERS)
    assert response.status_code == 404
