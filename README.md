# 🖪 Malangas Glass Inventory System

A modern inventory management system for a glass shop, built with Django.

---

## ✨ Features

* 📦 Product CRUD (Create, Read, Update, Soft Delete)
* 📁 CSV Import/Export for bulk product management
* 🟢 In-stock / 🔴 Out-of-stock status tracking
* 🔍 Product search and sorting
* 🗓️ Soft delete (archiving) and restore functionality
* 💻 Responsive, modern UI with seamless navigation

---

## ⚙️ Setup Instructions

### 🌀 1. Clone the Repository

```bash
git clone https://github.com/CaelumIsMe/finalsprojectElective.git
cd FinalsProject_django
```

### 🐍 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### 📦 3. Install Dependencies

```bash
pip install django
```

### 🛠️ 4. Run Migrations

```bash
python manage.py makemigrations
# If prompted for an app name, enter:
default
python manage.py migrate
```

### 👤 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 🚀 6. Start the Development Server

```bash
python manage.py runserver
```

### 🌐 7. Access the Web App

📬 Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 🧑‍💼 Usage

* 📝 **Add/Edit/Delete Products** from the product list page.
* 📅📄 **Import/Export CSV** for bulk product data.
* 💄️ **Archive/Restore Products** via the Archived Products page.
* 🔎 **Search/Sort** products easily using the search bar and sortable headers.

---

## 🗂️ Project Structure

```
FinalsProject_django/
🔝 glassapp/
📍   ├── models.py
📍   ├── views.py
📍   ├── forms.py
📍   ├── urls.py
📍   └── templates/
📍       └── glassapp/
📍           ├── index.html
📍           ├── product_list.html
📍           ├── product_form.html
📍           ├── product_confirm_delete.html
📍           ├── product_import.html
📍           ├── product_detail.html
📍           └── soft_deleted_products.html
📁 templates/
📍   └── base.html
📂 db.sqlite3
📚 manage.py
📓 README.md
```

---

## 🗄️ Screenshots

*Add screenshots of your UI here for a better presentation.*

---

## 📄 License

MIT

---

**Malangas Glass Inventory System** — Modern, efficient, and easy to use for any glass shop! 💎
