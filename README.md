# Product Management System (FastAPI Backend)

A robust and secure backend service for managing products (tasks) built with **FastAPI**, **SQLAlchemy ORM**, **PostgreSQL**, and secure password hashing & token authentication via **JWT**.

---

## 🚀 Key Features

*   **User Authentication & Security**:
    *   Secure registration with password hashing using the modern `pwdlib[argon2]` library.
    *   JWT-based user login generating secure access tokens with expiration support.
    *   Token authentication helper checking authorizations headers on protected endpoints.
*   **CRUD Operations for Products**:
    *   Retrieve all products, retrieve specific products by ID, create new products, update existing products, and delete products.
*   **Database Integration**:
    *   **PostgreSQL** integration powered by SQLAlchemy.
    *   Automatic table creation (`Base.metadata.create_all`).
    *   Database connection session lifecycle management using dependency injection.
*   **Structured Project Design**:
    *   Modular layout dividing the code cleanly into utility configurations (`src/Utils`), authentication & users (`src/Users`), and product management modules (`src/Tasks`).
    *   Environment variable management using `pydantic-settings`.

---

## 🛠️ Tech Stack & Dependencies

*   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
*   **Web Server**: [Uvicorn](https://www.uvicorn.org/)
*   **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
*   **Validation & Settings**: [Pydantic v2 & Pydantic Settings](https://docs.pydantic.dev/)
*   **Security & Hashing**: [pwdlib (Argon2)](https://pwdlib.readthedocs.io/)
*   **Tokens**: [PyJWT](https://pyjwt.readthedocs.io/)
*   **Database**: PostgreSQL

---

## 📁 Project Structure

```text
ProductManagementSystem_Using_FastApi/
├── .env                  # Local configuration & secrets
├── .gitignore            # Git exclusion settings
├── main.py               # Application entrypoint & initialization
├── requirements.txt      # Project Python dependencies
└── src/
    ├── Tasks/            # Tasks (Product) Module
    │   ├── Controllers.py# Endpoint controllers (logic)
    │   ├── dtos.py       # Pydantic validation schemas
    │   ├── Models.py     # SQLAlchemy Product models
    │   └── Routers.py    # Route definitions
    ├── Users/            # User Auth Module
    │   ├── Controllers.py# Register, login, & helper logic
    │   ├── dtos.py       # User input validation schemas
    │   ├── Models.py     # SQLAlchemy User models
    │   └── Routers.py    # Route definitions
    └── Utils/            # Database, settings & helpers
        ├── const.py      # Constant parameters
        ├── db.py         # DB connection & Session management
        ├── helper.py     # JWT & header authorization decorators
        └── settings.py   # Pydantic Settings loaders
```

---

## ⚙️ Configuration & Setup

### 1. Clone & Prerequisites
Make sure you have **Python 3.10+** and a running **PostgreSQL** database server.

### 2. Configure Environment Variables
Create a file named `.env` in the root folder (or customize the existing one):
```env
DATABASECONNECT=postgresql://username:password@localhost:5432/database_name
SECRET_KEY=your_generated_jwt_secret_key_hex
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Install Dependencies
Set up your virtual environment and install the required dependencies:
```bash
# Create and activate virtual environment
python -m venv env
source env/bin/activate # On Windows: env\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 4. Run the Application
Start the development server with Uvicorn:
```bash
uvicorn main:app --reload
```
The server will start on `http://127.0.0.1:8000`.

---

## 📡 API Endpoints

Once the application is running, you can explore the interactive API documentation at:
*   Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
*   ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 🔑 Authentication Routes (Prefix: `/auth`)

| Method | Endpoint | Description | Payload Schema |
|---|---|---|---|
| **POST** | `/auth/register` | Register a new user | `{ "name": "Name", "email": "email@example.com", "password": "password" }` |
| **POST** | `/auth/login` | Login to retrieve JWT access token | `{ "email": "email@example.com", "password": "password" }` |
| **GET** | `/auth/get` | Validate session token / get user details | Requires `Authorization: Bearer <token>` header |

### 📦 Task & Product Routes (Prefix: `/task`)
*All task routes require standard `Authorization: Bearer <token>` in headers.*

| Method | Endpoint | Description | Payload Schema |
|---|---|---|---|
| **GET** | `/task/` | Fetch all products / tasks | None |
| **POST** | `/task/create` | Create a new product | `{ "ProductTitle": "Title", "description": "Desc", "Price": "Price", "Comments": "Comment" }` |
| **GET** | `/task/get/{task_id}` | Fetch a single product by ID | None |
| **PUT** | `/task/updated/{task_id}` | Update product information | `{ "ProductTitle": "New Title", ... }` |
| **DELETE** | `/task/delete/{task_id}`| Delete a product by ID | None |

---

## 🛡️ Database Schema

Entities are hosted in PostgreSQL under the schema **`ProjectSchema`**.

### 1. User Register Model (`userRegister` Table)
*   `id`: `Integer` (Primary Key, Auto-incremented)
*   `name`: `String`
*   `email`: `String` (Unique, Not Null)
*   `password`: `String` (Hashed, Not Null)

### 2. Product/Task Model (`username` Table)
*   `id`: `Integer` (Primary Key, Auto-incremented)
*   `ProductTitle`: `String` (Not Null)
*   `description`: `String` (Not Null)
*   `Price`: `String`
*   `Comments`: `String`
