import httpx
from tools.fakers import fake

payload = {
    "email": fake.email(),
    "password": "Test12345",
    "lastName": "Uno",
    "firstName": "Savage",
    "middleName": "leo"
}
response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())
