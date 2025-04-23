# 🧠 Task Manager API

A lightweight and RESTful Django-based API to manage tasks, inspired by Unix-like process handling. It allows users to list, create, delete, and fork (duplicate) tasks easily.

---

## 📌 Project Overview

This API mimics Unix's `fork()` system call by allowing tasks to be "forked"—creating a copy of an existing task. It supports the following features:

- List all tasks
- Create a new task
- Fetch task details by ID
- Delete a task by ID
- Fork (duplicate) a task by ID

---

## ⚙️ Specifications

- **Framework:** Django 5.2
- **Database:** SQLite3 (default)
- **Language:** Python 3.12
- **Architecture:** RESTful API
- **Tooling:** Django REST Framework
- **Endpoints:**  
  - `GET /tasks/` - List tasks  
  - `POST /tasks/` - Create task  
  - `GET /tasks/<id>/` - View task  
  - `DELETE /tasks/<id>/` - Delete task  
  - `POST /tasks/<id>/fork/` - Fork a task

---

## 🛠️ Steps to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/taskmanager.git
   cd taskmanager
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   env\Scripts\activate   # For Windows
   # OR
   source env/bin/activate  # For Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the API**
   Open your browser or Postman and visit:
   ```
   http://127.0.0.1:8000/tasks/
   ```

---

## 📄 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this software with proper attribution.

---

## ✨ Author

Made with ❤️ by Subhashri