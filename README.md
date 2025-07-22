
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
pip install -r requirements.txt
```

### 4. Configure environment

Create a `.env` file in the root with the following:

```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://<username>:<password>@localhost:5432/<your_db_name>
```

Update `settings.py` to read from `.env` using `python-decouple`.

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

### 🔹 Upload Paragraphs (Protected)
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

### 🔹 Search Paragraphs by Word (Protected)
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
      "id": "para-uuid",
      "text": "The paragraph containing the word 'lorem'."
    }
  ]
}
```

---

## 📘 Documentation

### Swagger UI
> If using `drf-yasg`:

```
GET /swagger/ or /docs/
```

### Postman Collection

A ready-to-use collection is provided in the repository as:
```
postman_collection.json
```

---

## ✅ Example Input

```text
Lorem ipsum dolor sit amet...

Second paragraph text...

Third one here...
```

Searched word: `lorem` → Returns up to 10 paragraphs containing the word "lorem".

---

## 🧑 Author

**Name**: Alex Viju  
**Email**: alex@example.com  
**Submitted to**: Codemonk Backend Assignment – July 2025

---

## ✅ Deliverables Checklist

- [x] Custom User Model with JWT Auth
- [x] Paragraph & WordIndex Models
- [x] Upload Paragraph Endpoint
- [x] Word Search Endpoint (Top 10)
- [x] Auth-only access
- [x] README.md with full usage
- [x] Postman Collection or Swagger Docs

---

> ✅ Project complete and ready for review.
