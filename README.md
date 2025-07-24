# 🛍️ Product Review API

A Django REST Framework-based API for managing products and their reviews. Authenticated users can submit reviews, while admins manage the product catalog. One review is allowed per user per product, and products display aggregated average ratings.

---

## 🚀 Features

- 👤 **User Authentication** using token-based login
- 🛒 **Admin-managed Product Catalog**
- ✍️ **One Review per User per Product**
- 📊 **Average Product Ratings**
- 🔐 **Role-based Access Control**
- 🛡️ **Secure API Endpoints**

---

## 🧰 Tech Stack

- Python
- Django
- Django REST Framework
-  MySQL 

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/sohilzog/product-review-api.git
cd product-review-api

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. Create superuser (admin)
python manage.py createsuperuser

# 5. Start the development server
python manage.py runserver

## 🔑 API Endpoints

### 🔐 Authentication

| Method | Endpoint         | Description                  |
|--------|------------------|------------------------------|
| POST   | /api/register/   | Register a new user          |
| POST   | /api/token/      | Get auth token (login)       |

---

### 🛒 Products

| Method | Endpoint              | Description                |
|--------|-----------------------|----------------------------|
| GET    | /api/products/        | List all products          |
| POST   | /api/products/        | Add new product (Admin)    |
| PUT    | /api/products/{id}/   | Update product (Admin)     |
| DELETE | /api/products/{id}/   | Delete product (Admin)     |

---

### ✍️ Reviews

| Method | Endpoint              | Description                       |
|--------|-----------------------|-----------------------------------|
| GET    | /api/reviews/         | List all reviews                  |
| POST   | /api/reviews/         | Add a review (1 per product/user) |
| PUT    | /api/reviews/{id}/    | Update own review                 |
| DELETE | /api/reviews/{id}/    | Delete own review                 |

---

### 📊 Ratings

| Method | Endpoint                     | Description                |
|--------|------------------------------|----------------------------|
| GET    | /api/products/{id}/rating/   | Get product's avg rating   |

