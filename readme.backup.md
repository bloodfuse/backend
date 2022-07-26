# BloodFuse Backend Project

Reprehenderit mollit sint pariatur incididunt esse ea aliqua eiusmod. Do officia reprehenderit id exercitation ad. Eu occaecat ex labore Lorem qui id esse elit cillum. Mollit tempor sint est esse deserunt commodo laboris laboris quis.

# Technologies Used

- Programming Language: [**Python**](https://www.python.org)
- Framework: [**Django RestFramework (DRF)**](https://www.https://www.django-rest-framework.org/)
- Database: **Sqlite3**
- Development Hosting: [**PythonAnywhere**](https://www.pythonanywhere.com)

# Project Setup

Clone project

```console
git clone https://github.com/bloodfuse/backend/
```

Setup dev environment

```console
cd ./backend
pipenv install
pipenv shell
```

Start django server **(Linux/Mac)**

```console
python3 manage.py runserver
```

Start django server **(Windows)**

```console
python manage.py runserver
```

# API Endpoints URLs

- ## [Endpoints](https://bloodfuse.pythonanywhere.com/api/swagger/)
- ## [Docs](https://bloodfuse.pythonanywhere.com/api/redoc/)
- ## [Json](https://bloodfuse.pythonanywhere.com/api/swagger.json)
- ## [Yaml](https://bloodfuse.pythonanywhere.com/api/swagger.yaml)
-

# API Endpoints Docs

## Base Url

```console
https://bloodfuse.pythonanywhere.com/api/
```

## Authentication Endpoinsts

<!--
    [REGISTRATION]  ---------------------------------
 -->

- ### [/registration](#post-registration)
- ### [/token](#post-token)
- ### [/auth/login](#post-authlogin)
- ### [/auth/password/reset/]()

---

### POST [/registration/](https://bloodfuse.pythonanywhere.com/api/registration/)

#### Request

```markdown
#DESCRIPTION
Bloodfuse registration API requires some parameters to be passed as a post request.

#REQUIRED FIELDS
email, user_name, account_type, first_name, last_name, blood_group, password_1, password_2.

The account_type is of two options "donor" or "recipient", likewise the blood_group parameter also have some options to choose from, "O+", "O-", "A-", "A+", "B-", "B+", "AB-", "AB+".
When passing password_1 and password_2 both parameters must be the same else a 404 error is thrown.
```

```json
parameters: {
    "email":  "example@email.com",
    "username": "user1",
    "account_type": "donor",
    "first_name":  "Thomas",
    "last_name": "Edison",
    "blood_group": "O+",
    "password1": "1234567",
    "password2": "1234567"
}
```

#### Response

```json
method: GET,
response: {
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwODQyMjA0LCJpYXQiOjE2NjA4NDE5MDQsImp0aSI6ImI3MmQ2OGQyODNmZjQ2OTc4OTYxNWYxZmZhMWZjZjk4IiwidXNlcl9pZCI6IjJhMTZhMTFmLWY0ZmItNDRmYi1hYjExLWRmN2I3MjU3MjMwMSJ9.9dvTG2Hamo3a9gwiJ1aIve3j0Na7M8lEAEhbvBEOg8I",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MDkyODMwNCwiaWF0IjoxNjYwODQxOTA0LCJqdGkiOiI0NWY2Njg3MzYzZmE0NTkzYmUxODczMDA2YmY4Yzg2MyIsInVzZXJfaWQiOiIyYTE2YTExZi1mNGZiLTQ0ZmItYWIxMS1kZjdiNzI1NzIzMDEifQ.tpef4L3WluXVSguc5-ls4B8TOfxZSa1bAtrUwGvPtX0",
  "user": {
    "pk": "2a16a11f-f4fb-44fb-ab11-df7b72572301",
    "email": "gaddiel5@gmail.com",
   "first_name":  "Thomas",
    "last_name": "Edison",
  }
}
```

<!--
    [GET TOKENS]  ---------------------------------
 -->

## POST [token/](https://bloodfuse.pythonanywhere.com/api/token)

```json
description:
```

### Request

```json
parameters: {
    "email":  "example@exmaple.com",
    "password": "1234567890"
}
```

### Response

```json
method: GET
status: 200
response: {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MDg0ODQxNCwiaWF0IjoxNjYwNzYyMDE0LCJqdGkiOiI0MDMzNmVjYWNiMDk0YzBlYmU1OWJjZWY3MmM2OTdjZSIsInVzZXJfaWQiOiJkNDZiMTRmYy02MjAyLTRmMzktODNhNi00OWRjMWYxMDY3NmIifQ.TtCTWmtiRYsNiNmsrKeoDssIhCRE5eAToKuW9ZP-Mgs",

    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNzYyMzE0LCJpYXQiOjE2NjA3NjIwMTQsImp0aSI6ImUzMzRiYTFhODEzZTQxNzg5OTYyMjAzZjA5MzQ4OWYxIiwidXNlcl9pZCI6ImQ0NmIxNGZjLTYyMDItNGYzOS04M2E2LTQ5ZGMxZjEwNjc2YiJ9.4bdAPjRWKaJS6gb_le8A08Q_ri_tBM5ItRAuPtCOTJI"
}
```

<!--
    [LOGIN] ---------------------------------
 -->

## POST [auth/login/](https://bloodfuse.pythonanywhere.com/api/auth/login/)

```json
description:
```

### Request

```json
request: {
    "email":  "example@email.com",
    "password": "1234345"
}
```

### Response

```json
method: GET
status: 200
response: {
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNzY0NjM4LCJpYXQiOjE2NjA3NjQzMzgsImp0aSI6IjEwNDRiZTk0MmY4ODQwYjliMzFiNzMzYzZiOTZjZDA1IiwidXNlcl9pZCI6ImQ0NmIxNGZjLTYyMDItNGYzOS04M2E2LTQ5ZGMxZjEwNjc2YiJ9.KJsAKSK5StY72avNNWbhPZcsvBnUCXci4c3OBbj9wDs",

  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MDg1MDczOCwiaWF0IjoxNjYwNzY0MzM4LCJqdGkiOiI5NGEyMDViNTQzMzQ0ZTI4Yjk0YTY4MjFlZmRkMTkzZSIsInVzZXJfaWQiOiJkNDZiMTRmYy02MjAyLTRmMzktODNhNi00OWRjMWYxMDY3NmIifQ.0FTLJwSJZvt02X0zwdnEM6gluLSHE3SL_BJAnBA-Hzc",

  "user": {
    "pk": "d46b14fc-6202-4f39-83a6-49dc1f10676b",
    "email": "gaddiel@gmail.com",
    "first_name": "Gaddiel",
    "last_name": "Peterson"
  }
}
```

---

## Booking Endpoinsts

<!--
    [REGISTRATION]  ---------------------------------
 -->

- ### [/user/donor](#get-usersdonors)
- ### [/user/blood-centers](#get-usersblood-centers)

---

## GET [users/donors/](https://bloodfuse.pythonanywhere.com/api/auth/login/)

```json
description: This endpoint is protected therefore a supply of an access token is required to gain access.
```

### Request

```json
Request_Header: {
    ....
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNjQzNDYxLCJpYXQiOjE2NjE2NDMxNjEsImp0aSI6IjQxMmFiYmMxMzY3MzRiNTJiMzQyOWZkNTZiMGNiNzdhIiwidXNlcl9pZCI6ImU0NzFmNjZmLWMyN2MtNGEwYi1iOTFhLWY3MjU5Mzc3YTk5NCJ9.H7xlQXN8NJwi-QW22tLBueaFbNsszBzjAix-xwDxsW8"
}
```

### Response

```json
method: GET
status: 200
response: [
  {
    "id": "e471f66f-c27c-4a0b-b91a-f7259377a994",
    "email": "user3@example.com",
    "first_name": "james",
    "last_name": "bob",
    "account_type": "donor"
  },
  {/*  */
    "id": "e471f66f-c27c-4a0b-b91a-f725937342994",
    "email": "user3@example.com",
    "first_name": "peter",
    "last_name": "king",
    "account_type": "donor"
  },
  {
    "id": "e471f66f-c27c-4a0b-b91a-f725df47a994",
    "email": "user3@example.com",
    "first_name": "tom",
    "last_name": "riot",
    "account_type": "donor"
  },
]
```

## GET [users/blood-centers/](https://bloodfuse.pythonanywhere.com/api/auth/login/)

```json
description: This endpoint is protected therefore a supply of an access token is required to gain access.
```

### Request

```json
Request_Header: {
    ....
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNjQzNDYxLCJpYXQiOjE2NjE2NDMxNjEsImp0aSI6IjQxMmFiYmMxMzY3MzRiNTJiMzQyOWZkNTZiMGNiNzdhIiwidXNlcl9pZCI6ImU0NzFmNjZmLWMyN2MtNGEwYi1iOTFhLWY3MjU5Mzc3YTk5NCJ9.H7xlQXN8NJwi-QW22tLBueaFbNsszBzjAix-xwDxsW8"
}
```

### Response

```json
method: GET
status: 200
response: [
  {
    "id": "e471f66f-c27c-4a0b-b91a-f7259377a994",
    "email": "user3@example.com",
    "rc_number": "",
    "first_name": "james",
    "last_name": "bob",
    "rc_number": "",
    "account_type": "recipient"
  },
  {
    "id": "e471f66f-c27c-4a0b-b91a-f725937342994",
    "email": "user3@example.com",
    "rc_number": "",
    "first_name": "peter",
    "last_name": "king",
    "rc_number": "",
    "account_type": "recipient"
  },
  {
    "id": "e471f66f-c27c-4a0b-b91a-f725df47a994",
    "email": "user3@example.com",
    "rc_number": "",
    "first_name": "tom",
    "last_name": "riot",
    "rc_number": "",
    "account_type": "recipient"
  },
]
```
