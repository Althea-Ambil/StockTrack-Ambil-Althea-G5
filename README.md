# StockTrack – Livestock Monitoring and Record Management System

## Project Information

**Project Name:** StockTrack  
**Developer:** Althea Ambil  
**Section:** G5  
**Project:** Information Management 2 – Project Development 1

## Overview

StockTrack is a web-based Livestock Monitoring and Record Management System designed to help farmers manage their livestock information and related farm records.

The system is developed using Django as its full-stack web framework and Supabase PostgreSQL as its database.

## Technology Stack

- **Backend:** Python / Django
- **Frontend:** Django Templates, HTML, CSS, Bootstrap 5
- **Database:** Supabase PostgreSQL
- **Database Driver:** Psycopg 3
- **Image Processing:** Pillow
- **Environment Management:** Python-dotenv
- **Version Control:** Git and GitHub

## Implemented Features

### Account Management

- User registration for farmers
- Username and email validation
- Password confirmation
- Secure password hashing using Django authentication
- User login and logout
- Custom user model

### Role-Based Access Control

The system supports two user roles:

- **Administrator:** Access to the administrator dashboard.
- **Farmer:** Access to the farmer dashboard.

Each role has its own dashboard with restricted access to prevent unauthorized users from accessing another role's dashboard.

### User Dashboards

**Administrator Dashboard**
- User management overview
- System monitoring overview
- Account settings overview

**Farmer Dashboard**
- Livestock Profiling
- Breeding Management
- Livestock Selling

## Project Structure

```text
stocktrack/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── dashboard/
│   ├── migrations/
│   ├── templates/
│   │   └── dashboard/
│   │       ├── admin_dashboard.html
│   │       └── farmer_dashboard.html
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── accounts/
│   │   └── register.html
│   └── registration/
│       └── login.html
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Althea-Ambil/StockTrack-Ambil-Althea-G5.git
```

### 2. Navigate to the Project Directory

```bash
cd StockTrack-Ambil-Althea-G5
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the same directory as `manage.py`.

Add the following configuration:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True

DB_NAME=postgres
DB_USER=your-supabase-database-username
DB_PASSWORD=your-supabase-database-password
DB_HOST=your-supabase-pooler-host
DB_PORT=5432
```

Replace the placeholder values with your actual Django and Supabase credentials.

**Important:** Never upload your `.env` file or database credentials to GitHub.

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Create an Administrator Account

```bash
python manage.py createsuperuser
```

### 9. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

- Registration: http://127.0.0.1:8000/accounts/register/
- Login: http://127.0.0.1:8000/accounts/login/
- Admin Dashboard: http://127.0.0.1:8000/dashboard/admin/
- Farmer Dashboard: http://127.0.0.1:8000/dashboard/farmer/
- Django Admin: http://127.0.0.1:8000/admin/

## Security

- Passwords are securely hashed using Django's built-in authentication system.
- Role-based access restrictions protect dashboard pages.
- Database credentials and secret keys are stored in environment variables.
- The `.env` file and virtual environment are excluded from version control.

## Development Status

**Project Development 1 – Account Feature**

- [x] Django project setup
- [x] Supabase PostgreSQL configuration
- [x] Custom user model
- [x] Farmer registration
- [x] Login interface and authentication
- [x] Administrator dashboard
- [x] Farmer dashboard
- [x] Role-based dashboard protection
- [ ] User profile management
- [ ] Complete account feature testing

## Repository

GitHub: https://github.com/Althea-Ambil/StockTrack-Ambil-Althea-G5.git

---

**StockTrack**  
*Livestock Monitoring and Record Management System*