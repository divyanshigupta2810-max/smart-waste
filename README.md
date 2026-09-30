# 🗑️ Smart Waste Management System

A web-based **Smart Waste Management System** built using Flask that allows citizens to report waste-related issues and track their complaints, while administrators can manage complaints and update their status.

---

## 📌 About the Project

The Smart Waste Management System is designed to make waste complaint management easier and more organized.

Citizens can:

- Create an account
- Sign in securely
- Report waste-related issues
- Provide complaint details
- Track their complaint using a Complaint ID
- Check the current complaint status
- View the progress of their complaint

Administrators can:

- Sign in through the Admin Login
- View submitted complaints
- Check complaint details
- View complaint priority
- Update complaint status
- Monitor resolved and pending complaints

---

## ✨ Features

### 👤 Citizen

- 🔐 User Registration
- 🔑 User Login
- 📝 Report Waste Issue
- 🆔 Unique Complaint ID
- 🔎 Track Complaint
- 📊 Complaint Status Tracking
- 🚪 Logout

### 🛠️ Administrator

- 🔐 Admin Login
- 📋 View All Complaints
- 📊 Complaint Statistics
- ⚠️ Priority Management
- 🔄 Update Complaint Status
- ✅ Mark Complaints as Resolved
- 🚪 Admin Logout

---

## 🔄 Complaint Status Flow

```text
Submitted
    ↓
Under Review
    ↓
Assigned
    ↓
In Progress
    ↓
Resolved

Citizens can track the progress of their complaint using their Complaint ID.


---

🧑‍💻 Technology Stack

Frontend

HTML5

CSS3

Jinja2 Templates


Backend

Python

Flask

Flask-Login


Database

SQLite

SQLAlchemy / Flask-SQLAlchemy


Other

Werkzeug password hashing

UUID for unique identifiers



---

📂 Project Structure

Smart-Waste-Management/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   │
│   ├── templates/
│   │   ├── home.html
│   │   ├── login_choice.html
│   │   ├── register.html
│   │   ├── user_login.html
│   │   ├── admin_login.html
│   │   ├── dashboard.html
│   │   ├── admin_dashboard.html
│   │   ├── report.html
│   │   └── track_complaint.html
│   │
│   └── static/
│       ├── css/
│       ├── js/
│       └── uploads/
│
├── run.py
├── requirements.txt
├── README.md
└── instance/

> The exact folder structure may vary depending on the project configuration.




---

⚙️ Installation

1. Clone the repository

git clone https://github.com/divyanshigupta2810-max/smart-waste.git

2. Open the project

cd smart-waste-management

3. Create a virtual environment

Windows:

python -m venv venv

Activate it:

venv\Scripts\activate

Linux/macOS:

python3 -m venv venv
source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Run the application

python run.py

The application will usually be available at:

http://127.0.0.1:5000/


---

🔐 User Authentication

The system provides separate login options for:

Citizen

Citizens can register and sign in using their email and password.

Administrator

Administrators use the Admin Login section to access the administration dashboard.

Role-based access prevents users from accessing the wrong dashboard.


---

📝 Reporting a Complaint

A citizen can submit a waste complaint by providing information such as:

Waste category

Description

Location

Priority

Image (if enabled)


After submission, the system generates a unique Complaint ID.

Example:

SW-A83F21C4

This Complaint ID can be used to track the complaint.


---

🔎 Tracking Complaints

Citizens can enter their Complaint ID on the Track Complaint page.

The system displays:

Complaint ID

Category

Description

Priority

Current status

Submission date

Complaint progress



---

📊 Admin Dashboard

The administrator dashboard provides an overview of complaints.

It includes statistics such as:

Total Complaints
Pending Complaints
Resolved Complaints
High Priority Complaints

Administrators can also update the status of individual complaints.


---

🔄 Status Updates

When an administrator changes a complaint's status, the updated status is reflected when the citizen tracks the complaint.

Example:

Admin:
Status → In Progress

        ↓

Citizen:
Status → In Progress


---

🛡️ Security

The application includes:

Password hashing

Login authentication

Role-based authorization

Protected routes

Session-based authentication

Duplicate email checking


Passwords are not stored as plain text.


---

🚀 Future Improvements

Possible future improvements include:

📍 Interactive maps

📸 Better image management

🔔 Email/SMS notifications

📱 Mobile application

📊 Advanced analytics

🔎 Advanced complaint filtering

👥 Staff assignment

🗺️ Location-based complaint management

☁️ Cloud deployment

🎨 Improved responsive UI



---

🎯 Project Objective

The main objective of this project is to provide a simple digital platform for reporting and managing waste-related complaints.

It aims to improve communication between citizens and administrators and provide better visibility into the complaint resolution process.


---

👩‍💻 Developed With

Built as a web development project using:

Python + Flask + HTML + CSS + SQLite


---

📄 License

This project is created for educational and project purposes.
