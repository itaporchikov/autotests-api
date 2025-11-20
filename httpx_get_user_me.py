import httpx

login_payload = {
    "email": "ilya@gmail.com",
    "password": "Test12345"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

access_token = login_response_data['token']['accessToken']

client = httpx.Client(headers={"Authorization": "Bearer " + access_token})
user_response = client.get("http://localhost:8000/api/v1/users/me")
user_response_data = user_response.json()

print("User response:", user_response_data)
print("Status code:", user_response.status_code)
