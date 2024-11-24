# GenZon Backend Setup Guide

Welcome to the GenZon Backend! This guide will walk you through the steps to set up and run the application on your local machine.

---

## Prerequisites

Ensure you have the following installed on your system:

- **Python** (version 3.8 or higher)
- **Pip** (Python package manager)
- **Virtualenv** (optional but recommended)
- **Git**

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Ki55n/GenZon
cd genzon_backend
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
Since we're using the default SQLite database, Django will automatically use a file-based database (db.sqlite3).

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```
