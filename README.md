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

