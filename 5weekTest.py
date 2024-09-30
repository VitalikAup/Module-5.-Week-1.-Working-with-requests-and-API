import requests

# URLs для запросов
url1 = 'https://petstore.swagger.io/v2/user'
url2 = 'https://petstore.swagger.io/v2/user/TestAup1'
url3 = 'https://petstore.swagger.io/v2/user/TestAup1'

# Доздание нового юзера - url1
user_data = {
    "id": 0,
    "username": "TestAup1",
    "firstName": "Test",
    "lastName": "User",
    "email": "test@example.com",
    "password": "password",
    "phone": "1234567890",
    "userStatus": 1
}

# Выполнение запросов
response1 = requests.post(url1, json=user_data)  # Создание юзера
response2 = requests.get(url2)                    # Проверка юзера
response3 = requests.put(url2, json={"lastName": "UpdatedUser"})  # Обновление юзера

# Печать результата
print(f'Response from {url1}: {response1.status_code} - {response1.text}')
print(f'Response from {url2}: {response2.status_code} - {response2.text}')
print(f'Response from {url3}: {response3.status_code} - {response3.text}')


# session=requests.Session()
#
# response=session.get("http://httpbin.org/cookies/set?session_id=123456")
# print(response.status_code)
# print(response.text)
#
# response=session.get("http://httpbin.org/cookies")
# print(response.status_code)
# print(response.text)



# base_url = "http://httpbin.org/"
#
# endpoint = "/cookies"
# cookies = {
#     "location": "Barcelona"
# }
#
# response = requests.get(base_url + endpoint,cookies=cookies)
# print(response.status_code)
# print(response.text)



# url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available&status=available"

# payload = {}
# headers = {
#  'Accept': 'application/json'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
