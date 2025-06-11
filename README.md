# Malangas Glass Inventory System

A modern inventory management system for a glass shop, built with Django.

## Features
- Product CRUD (Create, Read, Update, Soft Delete)
- CSV Import/Export for bulk product management
- In-stock/Out-of-stock status tracking
- Product search and sorting
- Soft delete (archiving) and restore functionality
- Responsive, modern UI with seamless navigation

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd FinalsProject_django
```

### 2. Create and Activate a Virtual Environment (Recommended)
```
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```
pip install django
```

### 4. Run Migrations
```
python manage.py makemigrations
default
python manage.py migrate
```

### 5. Create a Superuser (Optional, for admin access)
```
python manage.py createsuperuser
```

### 6. Run the Development Server
```
python manage.py runserver
```

### 7. Access the App
- Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage
- **Add/Edit/Delete Products:** Use the product list page for all product management.
- **Import/Export CSV:** Use the buttons on the product list page to import/export products in bulk.
- **Archive/Restore Products:** Soft deleted products are moved to the archive. You can restore them from the "Archived Products" page.
- **Search/Sort:** Use the search bar and table headers to quickly find and organize products.

## Project Structure
```
FinalsProject_django/
├── glassapp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── glassapp/
│           ├── index.html
│           ├── product_list.html
│           ├── product_form.html
│           ├── product_confirm_delete.html
│           ├── product_import.html
│           ├── product_detail.html
│           └── soft_deleted_products.html
├── templates/
│   └── base.html
├── db.sqlite3
├── manage.py
└── README.md
```

## Screenshots
_Add screenshots of your UI here for a better presentation._

## License
MIT

---

**Malangas Glass Inventory System** — Modern, efficient, and easy to use for any glass shop!
