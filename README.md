# 🧳 JoBoard – Job Portal Web Application

JoBoard is a job portal web application built with Django. It allows **Job Seekers** to search and apply for jobs, **Employers** to post and manage job listings, and **Admins** to manage the platform.

---



## 🚀 Features

### 👤 User Roles
- **Job Seekers**: Register, log in, search jobs, apply for jobs
- **Employers**: Register, post jobs, manage listings
- **Admin**: Manage users and job listings through the Django Admin Panel

### 🛠️ Core Functionalities
- User authentication (register/login/logout)
- Job posting with:
  - Title
  - Description
  - Salary
  - Location
  - Job Type
  - Work Mode
  - Deadline
- Job search with filters:
  - Location
  - Job Type
  - Keyword search
- Job application system
- Admin panel to manage users and jobs
- Clean and responsive UI using Bootstrap

---

## 🧰 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap

---

Installation


# Clone the repo
git clone https://github.com/mad-jix/Joboard.git
cd Joboard

# (Optional) Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Run the server
python manage.py runserver