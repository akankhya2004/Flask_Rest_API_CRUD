# Task 4 - REST API with Flask

## Project Overview

This project is a simple REST API built with **Python and Flask** to manage user data.

The task requires a Flask application with **GET, POST, PUT and DELETE** routes. User data is stored in an **in-memory dictionary**, so no external database is required.

## Objectives

- Learn the basics of REST API development.
- Create Flask endpoints/routes.
- Work with JSON request and response data.
- Implement HTTP methods: GET, POST, PUT and DELETE.
- Handle common HTTP status codes such as 200, 201, 400 and 404.
- Test API endpoints using Postman or cURL.

## Technologies Used

- Python
- Flask
- JSON
- Postman / cURL
- Git & GitHub

## Project Structure

```text
task4_flask_rest_api/
│
├── app.py
├── requirements.txt
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-github-repo-link>
cd task4_flask_rest_api
```

### 2. Create a virtual environment (recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Flask

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/users` | Get all users |
| GET | `/users/<id>` | Get a specific user |
| POST | `/users` | Create a new user |
| PUT | `/users/<id>` | Update an existing user |
| DELETE | `/users/<id>` | Delete a user |

## Testing the API

You can use **Postman** or **cURL**.

### GET all users

```bash
curl http://127.0.0.1:5000/users
```

### GET one user

```bash
curl http://127.0.0.1:5000/users/1
```

### POST - Create a user

Use JSON body:

```json
{
    "name": "Priya",
    "email": "priya@example.com"
}
```

cURL:

```bash
curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d "{\"name\":\"Priya\",\"email\":\"priya@example.com\"}"
```

### PUT - Update a user

JSON body:

```json
{
    "name": "Priya Sharma",
    "email": "priyasharma@example.com"
}
```

cURL:

```bash
curl -X PUT http://127.0.0.1:5000/users/3 \
-H "Content-Type: application/json" \
-d "{\"name\":\"Priya Sharma\",\"email\":\"priyasharma@example.com\"}"
```

### DELETE - Delete a user

```bash
curl -X DELETE http://127.0.0.1:5000/users/3
```

## HTTP Status Codes Used

- **200 OK** - Request completed successfully.
- **201 Created** - A new user was created.
- **400 Bad Request** - Required JSON data is missing or invalid.
- **404 Not Found** - The requested user does not exist.

## Key Concepts Learned

### Flask
Flask is a lightweight Python web framework used to create web applications and APIs.

### REST API
A REST API allows applications to communicate using HTTP methods and resources.

### HTTP Methods

- **GET** - Read data.
- **POST** - Create data.
- **PUT** - Update data.
- **DELETE** - Remove data.

### `request.json`
`request.json` reads JSON data sent by the client in the request body.

### In-memory storage
The users are stored in a Python dictionary. This is simple for learning and testing, but the data will be lost when the Flask application is restarted.

## Future Improvements

- Replace the in-memory dictionary with SQLite/MySQL/PostgreSQL.
- Add input validation.
- Add authentication and authorization.
- Add automated API tests.
- Deploy the API to a cloud platform.

## Task Outcome

The project demonstrates the fundamentals of **Flask API development, REST, HTTP methods, JSON handling and basic CRUD operations**.
