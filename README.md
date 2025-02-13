# Django Project Setup Guide

##  Overview
This guide will help you set up and run a Django project from scratch. It covers installation, database setup, API testing, and running the server.

---

##  Getting Started

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/django-project.git
cd django-project
```

### **2️⃣ Set Up a Virtual Environment**
Ensure you have Python installed (version 3.8+ recommended).

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🛠 Database Setup

### **4️⃣ Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Create a Superuser (Admin Panel Access)**
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

---

##  Running the Project

### **6️⃣ Start the Development Server**
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

### **7️⃣ Access Django Admin Panel**
Go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.

---

##  API Testing with Postman

### **8️⃣ Test API Endpoints**
1. Open [Postman](https://www.postman.com/).
2. Use the following endpoints:
   - **Signup:** `POST http://127.0.0.1:8000/api/signup/`
   - **Login:** `POST http://127.0.0.1:8000/api/signin/`
   - **Forgot Password:** `http://127.0.0.1:8000/api/profile/forgot-password/`
   - **Update Profile:** `PUT http://127.0.0.1:8000/api/update-profile/`
   - **Google Login:** `POST http://127.0.0.1:8000/api/google-login/`
3. Use **JSON** format for requests.

Example request body for **Signup**:
```json
{
  "username": "mgasa",
  "firstname": "Mgasa",
  "lastname": "Lucas",
  "gender": "Male",
  "email": "mgasa@quantumintelligence.co.tz",
  "password": "securedpassword",
  "confirm_password": "securedpassword"
}
```

---

## 📂 Project Structure
```
project-root/
│── config/          # Project configuration (settings, urls, wsgi, asgi)
│── profiles_manager/ # User profile app (views, models, serializers, urls)
│── static/          # Static files (CSS, JS, images)
│── templates/       # HTML templates
│── manage.py        # Django project management script
│── requirements.txt # Dependencies
│── README.md        # This guide
```

---

##  Deployment (Optional)
For production deployment:
```bash
python manage.py collectstatic
```
Use **Gunicorn**, **Nginx**, or **Docker** for deployment.

---

## ✅ Common Issues & Fixes
### **1️⃣ Virtual Environment Not Activating?**
- Ensure you’re in the correct directory and use the right activation command.

### **2️⃣ Migrations Not Working?**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **3️⃣ Server Port Conflict?**
Use another port:
```bash
python manage.py runserver 8080
```

---

## 📞 Support
For issues, open a GitHub issue or contact developers and contributors : mgasa@quantumintelligence.co.tz

---

### 🎉 Happy Coding!

