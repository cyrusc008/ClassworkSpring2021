import requests

patient = {"name": "John Wick",
           "id": 8,
           "blood_type": "AB-"}

test = {"id": 1000,
        "test_name": "ECG",
        "test_result": 0}

r = requests.post("http://127.0.0.1:5000/new_test", json=test)
print(r.status_code)
print(r.text)
