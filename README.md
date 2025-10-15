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


3. Installation & Setup
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

4. Sample Data
    You can add more data through the Django admin panel at: http://127.0.0.1:8000/admin/
    Or manually add records via the interface.

5. Requirements
    Please refer to the requirement.txt file

6. Author
    Ho Khai Liang
    hokhailiang1215@gmail.com# ClientOrderManagementSystem
