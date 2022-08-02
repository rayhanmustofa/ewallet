# Ewallet Documentation

Note : This is my first time using python & django 

## Endpoints :

List of available endpoints:

- `GET /api/user-list/`
- `GET /api/history-list/`
- `POST /api/user-create/`
- `PUT /api/user-topup/<int:pk>/`
- `PUT /api/user-transfer/<int:pk>/`

&nbsp;

## 1. GET /api/user-list/

Description:

- Get the list of all registered users

_Response (200 - OK)_

```json
{
  "status": 200,
  "data": [
    {
      "id": 1,
      "name": "user1",
      "balance": "300000.00"
    },
    {
      "id": 2,
      "name": "user2",
      "balance": "450000.00"
    },
    {
      "id": 3,
      "name": "user3",
      "balance": "291000.00"
    }
  ]
}
```

## 2. GET /api/history-list/

Description:

- Get the list of transaction (top-up & transfer) history

_Response (200 - OK)_

```json
{
  "status": 200,
  "data": [
    {
      "id": 1,
      "description": "Top up amount 777 by user with ID : 1",
      "date": "2022-08-01T00:00:00Z",
      "userId": 1
    },
    {
      "id": 2,
      "description": "Top up amount 100 by user with ID : 1",
      "date": "2022-08-01T16:32:20.523800Z",
      "userId": 1
    }
  ]
}
```

## 3. POST /api/user-create/

Description:

- Create a new User

Request:

- body:

```json
{
  "name": "user3",
  "balance": "300000"
}
```

_Response (201 - Created)_

```json
{
  "status": 201,
  "message": "Success creating new user!",
  "data": {
    "id": 4,
    "name": "user4",
    "balance": "300000.00"
  }
}
```

&nbsp;

## 4. PUT /api/user-topup/<int:pk>/

Description:

- Top-up the balance of a User

Request:

- params:

```json
{
  "id": "integer (required)"
}
```

- body:

```json
{
  "topup": "integer"
}
```

_Response (200 - OK)_

```json
{
  "status": 200,
  "message": "Top-Up Success!",
  "data": {
    "id": 4,
    "name": "user4",
    "balance": "400000.00"
  }
}
```

_Response (404 - Not Found)_

```json
{
  "message": "Movie not found"
}
```

&nbsp;

## 5. PUT /api/user-transfer/<int:pk>/

Description:

- Transfer balance from one user to another.

Request:

- params:

```json
{
  "id": "integer (required)"
}
```

- body:

```json
{
  "idTo": "integer (required)",
  "amount": "integer"
}
```

_Response (200 - OK)_

```json
{
  "status": 200,
  "message": "Success transferring 5000 from User with ID : 1 to User with ID : 2"
}
```

&nbsp;
