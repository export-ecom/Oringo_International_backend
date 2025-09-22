# Ecom Export Backend (Django + DRF)

This is the backend service for the Ecom Export project, built with **Django** and **Django REST Framework (DRF)**.  
It provides APIs for user authentication, profile management, products, cart, orders, payments, and blogs.

---

## 🚀 Features
- User Registration (`/api/register/`)
- JWT Authentication (Login, Refresh, Logout)
- Profile Management 
- Add Products, Cart, Order,Quotations and Payment APIs
- Blog API
- Celery + Redis for background task processing

---

## 🛠️ Tech Stack
- **Python 3.x**
- **Django 5.x**
- **Django REST Framework**
- **Simple JWT** for authentication
- **Celery + Redis** for asynchronous tasks
- **SQLite**

---

## Installation & Setup

### 1. Clone the repository
git clone https://github.com/export-ecom/Oringo_International_backend.git

## 2. Create & activate virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

## 3. Install dependencies
pip install -r requirements.txt

## 4. Run migrations
python manage.py migrate

## 5. Create superuser (for Django Admin)
python manage.py createsuperuser

## 6. Run development server

python manage.py runserver
Server will be running at:
👉 http://127.0.0.1:8000/


-- Celery & Redis Setup --

## Since Redis doesn’t run natively on Windows, you need to install and run it inside **WSL (Ubuntu/Debian)**.

## 1. Install Redis inside WSL
## 2. Start Redis

redis-server

## 3. Start Celery Worker
## Run this command from your project root (where celery.py is located)

celery -A root_folder worker --pool=solo -l info
