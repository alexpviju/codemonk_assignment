
# 📘 Codemonk Assignment – Paragraph Indexing & Search API

A secure Django REST API that accepts multi-paragraph input, indexes words per paragraph, and enables authenticated users to search for top 10 matching paragraphs by word.

---

## 🚀 Features

- Custom User Model (UUID, name, email, DOB, created/modified timestamps)
- JWT Authentication (Register & Login)
- Paragraph Upload API:
  - Accepts multiple paragraphs separated by `\n\n`
  - Tokenizes and lowercases words
  - Stores paragraph and word–paragraph mapping
- Search API:
  - Returns top 10 paragraphs containing a searched word
- PostgreSQL database integration
- Swagger/Postman API documentation

---

## 🛠️ Tech Stack

- Python, Django, Django REST Framework
- PostgreSQL
- JWT Authentication (`djangorestframework-simplejwt`)
- API Docs: Swagger via `drf-yasg` (or Postman collection)

---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/codemonk_assignment.git
cd codemonk_assignment
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install django
pip install djangorestframework
pip install psycopg2-binary
pip install python-decouple
pip install djangorestframework-simplejwt
pip install drf-yasg
```

### 4. Configure environment

Create a `.env` file in the root with the following:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

DB_NAME=paragraphdb
DB_USER=postgres
DB_PASSWORD=Alex@2001
DB_HOST=localhost
DB_PORT=5432
```

Update `settings.py` to read from `.env` using `python-decouple`like below.
```
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the server
```bash
python manage.py runserver
```

---

## 🔑 Authentication

- **Register**: `POST /api/auth/register/`
- **Login**: `POST /api/auth/login/`

You will receive an access and refresh token. Use the access token in the `Authorization` header for all protected requests:

```
Authorization: Bearer <your_access_token>
```

---

## 📦 API Endpoints

### 🔹 Register
```http
POST /api/auth/register/
```
```json
{
  "name": "Alex",
  "email": "alex@example.com",
  "dob": "2000-01-01",
  "password": "yourpassword"
}
```

---

### 🔹 Login
```http
POST /api/auth/login/
```
```json
{
  "email": "alex@example.com",
  "password": "yourpassword"
}
```

---

### 🔹 Upload Paragraphs seperated by \n\n
```http
POST /api/auth/paragraphs/
```
**Headers**: `Authorization: Bearer <access_token>`

```json
{
  "text": "First paragraph content.\n\nSecond paragraph content."
}
```

**Response**
```json
{
  "message": "2 paragraphs indexed successfully."
}
```

---

### 🔹 Search Paragraphs by Word 
```http
POST /api/auth/search/
```
**Headers**: `Authorization: Bearer <access_token>`

```json
{
  "word": "lorem"
}
```

**Response**
```json
{
  "word": "lorem",
  "results": [
    {
      "id": "1",
      "text": "The paragraph containing the word 'lorem'."
    }
  ]
}
```

---


##📁 Download Postman Collection: [postman_collection.json](./postman_collection.json)


## 🧑 Author

**Name**: Alex Viju  
**Email**: alex@example.com  
**Submitted to**: Codemonk Backend Assignment

