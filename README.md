Client Order Management System (Django Case Study)

1. Description
    The Client Order Management System is a web-based platform developed using Django to help consulting firms efficiently manage clients and their orders.
    It provides CRUD operations for both Clients and Orders, an total view Dashboard, and supports client and order search, filtering, CSV export, and pagination.

2. Features
    a. User Authentication
        -   Built-in Django authentication system.
        -   Only logged-in users can access the system.
        -   Admin users can manage all data.
        -   Normal users can add and view orders only.

    b. Client Management
        -   Add, edit, delete client records.
        -   Search clients by name or company.
        -   Export client data as CSV.

    c. Order Management
        -   Add, edit, delete orders.
        -   Filter orders by client or status.
        -   View all orders with client name, amount, and order status.
        -   Export order data as CSV.

    d. Dashboard
        -   Displays total clients and total orders.
        -   Shows order count by status (Pending, In Progress, Completed).

    e. Additional Features
        -   Responsive UI.
        -   Pagination for long lists.
        -   Clean, modular Django MVC structure.


3. Project Structure
CLIENTORDERPROJECT_KPMG
│
├── manage.py                              (Django command-line tool to run and manage the project)
├── db.sqlite3                             (SQLite database storing all client and order data)
├── requirements.txt                       (List of all required Python packages)
├── README.md                              (Project overview, setup, and usage guide)
│
├── clientOrderManagementSystem/           (Main Django project configuration folder)
│   ├── __init__.py                        (Marks folder as a Python package)
│   ├── settings.py                        (Project settings: database, apps, templates, static files)
│   ├── urls.py                            (Main URL router linking to app URLs)
│   ├── wsgi.py                            (WSGI entry point for production deployment)
│   ├── asgi.py                            (ASGI entry point for async deployment)
│
├── core/                                  (Main Django app handling clients and orders)
│   ├── __init__.py                        (Marks folder as a Python package)
│   ├── admin.py                           (Registers Client and Order models in Django admin)
│   ├── apps.py                            (App configuration for Django)
│   ├── forms.py                           (Contains ClientForm and OrderForm for input handling)
│   ├── models.py                          (Defines Client and Order database models)
│   ├── urls.py                            (Defines app-level URLs for CRUD operations)
│   ├── views.py                           (Handles logic for lists, forms, delete, and CSV export)
│   ├── tests.py                           (Contains unit tests — currently minimal)
│
│   ├── migrations/                        (Tracks database schema changes)
│   │   ├── __init__.py                    (Marks folder as a Python package)
│   │   ├── 0001_initial.py                (Initial migration creating base models)
│   │   ├── 0002_alter_client_company_alter_client_name.py (Model update migration)
│   │   ├── 0003_alter_order_status.py     (Migration updating order status field)
│
│   ├── templates/                         (HTML templates for rendering views)
│   │   ├── base.html                      (Base layout shared by all templates)
│   │
│   │   ├── core/                          (App-specific templates)
│   │   │   ├── dashboard.html             (Displays summary stats and overview)
│   │   │   ├── client_list.html           (Shows all clients with search and pagination)
│   │   │   ├── client_form.html           (Form for adding or editing a client)
│   │   │   ├── client_confirm_delete.html (Confirm client deletion page)
│   │   │   ├── order_list.html            (Displays all orders with pagination/filter)
│   │   │   ├── order_form.html            (Form for adding or editing an order)
│   │   │   ├── order_confirm_delete.html  (Confirm order deletion page)



4. Installation & Setup
    a. Clone the Repository
        git clone https://github.com/yourusername/CLIENTORDERPROJECT_KPMG.git
        cd CLIENTORDERPROJECT_KPMG

    b. Create a Virtual Environment
        python -m venv venv
        venv\Scripts\activate     

    c. Install Dependencies
        pip install -r requirements.txt

    d. Run Migrations
        python manage.py migrate

    e. Create Superuser
        python manage.py createsuperuser

    f. Run the Server
        python manage.py runserver

    g. open your browser and visit: http://127.0.0.1:8000/

5. Sample Data
    You can add more data through the Django admin panel at: http://127.0.0.1:8000/admin/
    Or manually add records via the interface.

6. Requirements
    Please refer to the requirement.txt file

7. Author
    Ho Khai Liang
    hokhailiang1215@gmail.com