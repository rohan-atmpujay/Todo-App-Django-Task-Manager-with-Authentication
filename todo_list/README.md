# Todo-App-Django-Task-Manager-with-Authentication

A simple yet complete Todo List Web Application built using Django.
It includes User Authentication, Task Management (CRUD), and a clean, modern UI with custom CSS styling.

This project is perfect for beginners learning Django or anyone wanting a lightweight personal task manager.

🚀 Features
🔐 User Authentication

Signup

Login

Logout

Logged-in users cannot access login/signup pages

Protected routes using @login_required

🗂️ Task Management (CRUD)

Create tasks

Read: Full task details page

Update: Edit existing tasks

Delete: Remove tasks

Each task contains:

Task title

Description

Last date (deadline)

Linked to the logged-in user

🎨 Modern UI

Fully styled pages:

Home page with task cards

Add Task

Edit Task

Description Page

Login

Signup

Clean and responsive CSS

Consistent UI across all screens

🛠️ Tech Stack

Backend: Django 5.x

Frontend: HTML, CSS

Database: SQLite (default Django DB)

📂 Folder Structure
todo_list/
    todo_app/
        templates/
            base.html
            home.html
            login.html
            signup.html
            add_task.html
            edit_task.html
            description.html
        models.py
        views.py
        urls.py
    todo_list/
        settings.py
        urls.py

⚙️ How to Run This Project
1️⃣ Clone the repository:
git clone https://github.com/rohan-atmpujay/Todo-App-Django-Task-Manager-with-Authentication

2️⃣ Navigate into the project:
cd todo-app

3️⃣ Create and activate a virtual environment:
python -m venv venv
venv/Scripts/activate  # On Windows

4️⃣ Install dependencies:
pip install django

5️⃣ Run migrations:
python manage.py migrate

6️⃣ Start the development server:
python manage.py runserver

7️⃣ Open in browser:
http://127.0.0.1:8000/

🙌 Contributions

Feel free to fork the repo and submit pull requests with improvements—UI enhancements, new features, or code cleaning are welcome!

