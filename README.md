# Product Management System (FastAPI)

A production-ready FastAPI backend using MVC architecture, PostgreSQL, SQLAlchemy ORM, and JWT authentication.

## Features

- User registration and login with JWT (Argon2 password hashing via pwdlib)
- Password complexity validation
- Full product CRUD scoped to the authenticated user
- Consistent JSON response format
- Swagger UI with OAuth2 Bearer token support

## Project Structure

```
src/
├── Users/          # User authentication module
├── Products/       # Product management module
├── Utils/          # Database, auth, settings, dependencies
└── main.py         # FastAPI application entry point
```

## Setup

1. Create a PostgreSQL database and ensure the `ProjectSchema` schema exists:

```sql
CREATE SCHEMA IF NOT EXISTS "ProjectSchema";
```

2. Copy environment variables:

```bash
cp .env.example .env
```

3. Update `.env` with your PostgreSQL credentials and a secure `SECRET_KEY`.

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
uvicorn src.main:app --reload
```

6. Open Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Authentication in Swagger

1. Register a user via `POST /users/register`
2. Click **Authorize** and use `POST /users/login` (enter your **email** as the username field)
3. Access protected product endpoints with the returned Bearer token

## API Endpoints

| Method | Endpoint            | Auth Required |
|--------|---------------------|---------------|
| POST   | /users/register     | No            |
| POST   | /users/login        | No            |
| POST   | /products           | Yes           |
| GET    | /products           | Yes           |
| GET    | /products/{id}      | Yes           |
| PUT    | /products/{id}      | Yes           |
| DELETE | /products/{id}      | Yes           |

## Response Format

**Success:**

```json
{
  "success": true,
  "message": "Product created successfully",
  "data": {}
}
```

**Error:**

```json
{
  "success": false,
  "message": "Unauthorized"
}
```
