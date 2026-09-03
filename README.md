# Flask User Management REST API

This is a simple REST API created using Python and Flask. It manages user data using GET, POST, PUT, and DELETE methods.

## Requirements

```bash
python -m pip install flask
```

## Run the Project

```bash
python app.py
```

Open this URL in your browser:

```text
http://127.0.0.1:5000/users
```

## API Routes

| Method | Route | Description |
|---|---|---|
| GET | `/users` | Get all users |
| GET | `/users/1` | Get one user |
| POST | `/users` | Add a user |
| PUT | `/users/1` | Update a user |
| DELETE | `/users/1` | Delete a user |

## Sample User

```json
{
  "id": 1,
  "name": "Raj",
  "email": "raj@example.com"
}
```

## Author

Kunal Singh Rajpoot
