
# StockTrack – Livestock Monitoring and Record Management System

## Project Information

- **Project Name:** StockTrack
- **Developer:** Althea Ambil
- **Section:** G5
- **Course:** Information Management 2
- **Project Phase:** Project Development 3 (PD3)
- **Repository:** https://github.com/Althea-Ambil/StockTrack-Ambil-Althea-G5

## Overview

StockTrack is a web-based Livestock Monitoring and Record Management System designed to help farmers manage livestock information and related farm records.

The system is developed using Python and Django, with Supabase PostgreSQL as its database.

This PD3 version focuses on improving the security, validation, reliability, and integrity of the existing core features without introducing new major features.

## Technology Stack

- **Backend:** Python / Django
- **Frontend:** Django Templates, HTML, CSS, Bootstrap 5
- **Database:** Supabase PostgreSQL
- **Database Driver:** Psycopg 3
- **Image Processing:** Pillow
- **Environment Management:** Python-dotenv
- **Version Control:** Git and GitHub

## Main Features

### 1. Account Management

- Farmer registration
- Username and email validation
- Password confirmation
- Secure password hashing through Django authentication
- User login and logout
- User profile management
- Custom user model

### 2. Role-Based Access Control

The system supports two user roles:

- **Administrator:** Can access the administrator dashboard.
- **Farmer:** Can access the farmer dashboard.

Unauthorized users are prevented from accessing dashboards assigned to other roles.

### 3. User Dashboards

**Administrator Dashboard**
- User management overview
- System monitoring overview
- Account settings overview

**Farmer Dashboard**
- Livestock Profiling
- Breeding Management
- Livestock Selling

### 4. Livestock Profiling

- Create livestock records
- View livestock records
- Update livestock records
- Delete livestock records
- Search livestock records
- Validate livestock information

## PD3 Improvements

The following improvements were implemented during Project Development 3.

### Server-Side Validation

- Added validation for required livestock information.
- Prevented duplicate livestock tag numbers.
- Added positive livestock weight validation.
- Prevented future birth and acquisition dates.
- Prevented acquisition dates earlier than birth dates.
- Added first and last name validation in profile updates.
- Improved duplicate email validation.

### Security Improvements

- Added login requirements to protected views.
- Restricted dashboard access according to user roles.
- Prevented farmers from accessing other farmers' livestock records.
- Restricted profile updates to permitted account fields.
- Ensured farmer registration assigns the FARMER role.
- Used CSRF protection for POST forms.
- Used POST requests for deletion and logout.
- Used Django ORM for database operations.
- Kept sensitive configuration in environment variables.

### Database Integrity

- Added livestock model constraints.
- Used transactions for livestock create, update, and delete operations.
- Used appropriate object retrieval and access filtering.
- Added custom 404 and 500 error pages.
- Used redirects after successful form submissions.

## Installation and Setup

### Prerequisites

Install the following before running the project:

- Python
- Git
- A Supabase PostgreSQL database

### 1. Clone the Repository

```bash
git clone https://github.com/Althea-Ambil/StockTrack-Ambil-Althea-G5.git
```

Navigate to the project directory:

```bash
cd StockTrack-Ambil-Althea-G5
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Add the following variables using your own credentials:

```env
SECRET_KEY=your-django-secret-key
DEBUG=False

DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=your-database-host
DB_PORT=5432
```

**Important:** Never upload your `.env` file or database credentials to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open the application:

```text
http://127.0.0.1:8000/
```

## Testing

StockTrack includes automated Django tests covering account management, dashboard access, livestock validation, and security.

Run all project tests:

```bash
python manage.py test --keepdb
```

Run tests for individual applications:

```bash
python manage.py test accounts --keepdb
python manage.py test dashboard --keepdb
python manage.py test livestock --keepdb
```

Check the Django project configuration:

```bash
python manage.py check
```

### PD3 Test Results

The complete test suite passed during PD3 development:

| Application | Tests Passed |
|---|---:|
| Accounts | 9 |
| Dashboard | 9 |
| Livestock | 10 |
| **Total** | **28** |

Command used:

```bash
python manage.py test --keepdb
```

## Project Structure

```text
stocktrack/
│
├── accounts/
│   ├── migrations/
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
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
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── livestock/
│   ├── migrations/
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── accounts/
│   ├── registration/
│   ├── 404.html
│   └── 500.html
│
├── docs/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Version Control

The project uses Git and GitHub for version control.

PD3 development workflow:

- `main` – Main project branch.
- `develop` – Integration branch.
- `fix/validation-errors` – Livestock validation and security.
- `fix/profile-security` – Account registration and profile security.
- `fix/dashboard-security` – Dashboard role-based access control.

Three work branches were merged into `develop`, followed by a final pull request merging `develop` into `main`.

## Security Notice

- Do not commit `.env` files.
- Do not expose database passwords or Django secret keys.
- Use environment variables for sensitive configuration.
- Keep DEBUG disabled when using production settings.
- Use proper authentication and authorization checks.

## License

This project was developed for academic purposes as part of Information Management 2.
