# Setting Up Inmest Project

Follow these steps to set up your Django project environment, start your project, and perform initial configurations:

## 1. Setting Up the Environment

1. **Open Command Prompt (CMD):** Press `Win + R`, type `cmd`, and hit `Enter`.

2. **Navigate to Your Project Folder:**
   ```bash
   cd django\inmest_app_api
   ```

3. **Create a Virtual Environment:**
   ```bash
   python -m venv my_nenv
   ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     my_nenv\Scripts\activate
     ```

## 2. Installing Django

1. **Install Django:**
   ```bash
   python -m pip install Django
   ```

## 3. Starting Your Django Project

1. **Create Your Django Project:**
   ```bash
   django-admin startproject inmest_2024_api .
   ```
   Note: The period (`.`) at the end of the command specifies that the project should be created at the current directory's root.

## 4. Running the Development Server

1. **Start the Server:**
   ```bash
   python manage.py runserver
   ```

2. **Navigate to the Admin Dashboard:**
   - Open your web browser and go to `http://127.0.0.1:8000/admin`

## 5. Making and Applying Migrations

1. **Create Migrations for Your Models:**
   ```bash
   python manage.py makemigrations
   ```

2. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

## 6. Creating a Superuser

1. **Create a Superuser Account:**
   ```bash
   python manage.py createsuperuser
   ```
   - Follow the prompts to set up a username, email, and password for the superuser account.
     
## 7. Creating Main and Users models
