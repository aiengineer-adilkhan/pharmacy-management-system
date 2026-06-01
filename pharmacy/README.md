# Pharmacy Management System

A full-featured Pharmacy Management System developed using Django, MySQL, HTML, and CSS. The system provides secure authentication, role-based access control, inventory management, customer management, supplier management, employee management, purchase tracking, sales processing, and reporting.

## Features

### Authentication & Security

* Secure user login and logout
* Django Authentication System
* Password-protected access
* Session management

### Role-Based Access Control (RBAC)

Three user roles are implemented:

#### Admin

* Manage Medicines
* Manage Customers
* Manage Suppliers
* Manage Employees
* Manage Purchases
* Manage Sales
* Access Reports

#### Pharmacist

* Manage Medicines
* Manage Customers
* Manage Purchases
* Manage Sales
* View Reports

#### Cashier

* Manage Customers
* Manage Sales

### Medicine Management

* Add Medicines
* Update Medicines
* Delete Medicines
* View Inventory
* Track Stock Quantity

### Customer Management

* Add Customers
* Edit Customer Information
* Delete Customers
* View Customer Records

### Supplier Management

* Add Suppliers
* Edit Supplier Information
* Delete Suppliers
* View Supplier Records

### Employee Management

* Add Employees
* Edit Employee Information
* Delete Employees
* View Employee Records

### Purchase Management

* Record Purchases
* Update Inventory Automatically
* Track Purchase History

### Sales Management

* Record Sales
* Reduce Inventory Automatically
* Track Sales History

### Reporting Dashboard

* Total Medicines
* Total Customers
* Total Suppliers
* Total Employees
* Total Purchases
* Total Sales

---

## Technology Stack

### Backend

* Python
* Django

### Database

* MySQL

### Frontend

* HTML
* CSS

### Authentication

* Django Authentication System
* Django Groups & Permissions

---

## Project Structure

```text
Pharmacy Management System
│
├── pharmacy_project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── pharmacy
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates
│   └── static
│
├── manage.py
└── requirements.txt
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/pharmacy-management-system.git
cd pharmacy-management-system
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Update database settings in:

```python
settings.py
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pharmacy_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## User Roles

### Admin

Full system access.

### Pharmacist

Medicine, Purchase, Sales, Customer, and Reports access.

### Cashier

Customer and Sales access only.

---

## Learning Outcomes

This project demonstrates:

* Database Design
* CRUD Operations
* Django Framework
* MySQL Integration
* Authentication & Authorization
* Role-Based Access Control (RBAC)
* Inventory Management
* Software Engineering Fundamentals

---

## Future Improvements

* Invoice Generation
* PDF Reports
* Barcode Scanner Integration
* Email Notifications
* Data Visualization Charts
* Cloud Deployment
* REST API Development

---

## Author

**Adil Khan**

BS Artificial Intelligence

Machine Learning & Web Development Enthusiast

GitHub: https://github.com/aiengineer-adilkhan
