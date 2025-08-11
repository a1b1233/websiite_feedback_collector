# 🌐 Feedback Collector Web App with Admin Dashboard

A user-friendly web application built with **Flask**, **HTML/CSS**,**Javascript** and **SQLite** that allows users to submit feedback and enables admin to review and update feedback status via a secure dashboard. Automated email notifications are also sent during submission and resolution.

---

## 🚀 Features

- 📝 Submit feedback with name, email, rating, and comment
- 📩 Email notification after feedback submission
- 🔐 Admin login for secure access to dashboard
- 📊 Admin dashboard to view and manage feedback
- ✅ Update feedback status and notify users via email
- 🔎 Users can check status of their submitted feedback
- 💡 Responsive design with custom styling

---

## 🛠 Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| 🧠 Backend   | Python (Flask)      |
| 🌐 Frontend | HTML, CSS, JS       |
| 🗄 Database | SQLite              |
| 📬 Emails   | Gmail SMTP + Python |

---

## 📦 Folder Structure

```
project/
├── app.py                  # Main Flask app
├── static/
│   └── style.css           # Custom styles
├── screenshots/
│   ├── admin-login.png
|   ├──check-status.png
│   ├── dashboard.png
│   ├── email.png
│   ├── feedback-status.png
│   └── feedback-status-resolved.png 
│   ├── homepage.png
|   ├──resolved.png
│   ├── thank-you.png
├── templates/
│   ├── admin_login.html
|   ├──admin-dashboard.html
│   ├── check_status.html
│   ├── feedback_status.html
│   ├── thank_you.html
│   └── index.html        # Assumed to be homepage with feedback form
├── README.md               # This file
└── API.md     # Full API details
```

---

## 🔐 Admin Credentials (Hardcoded for Demo)

```
Email: gs7august@gmail.com
Password: 8052566305
```

---

## ✉️ Email Notification

- Sent using `smtplib` and Gmail's SMTP server
- Emails sent when:
  - A user submits feedback (confirmation)
  - Admin updates feedback status (notification)

Credentials used in `app.py`:

```python
EMAIL_ADDRESS = "gs7august2005@gmail.com"
EMAIL_PASSWORD = "**** **** **** ****"
```

---

## 🧪 Running the App Locally

### 🔧 Prerequisites

- Python 3.7+

---

### 📥 Steps

1. **Clone the Repository or Copy the Code**

2. **Install Required Packages**

```bash
pip install flask flask_sqlalchemy
```

3. **Run the Flask App**

```bash
python app.py
```

4. **Open your browser** and visit:

[http://localhost:5000](http://localhost:5000)

---

## 📚 Documentation

- [✅ API Documentation (Markdown)](./API.md)

## 📸 Screenshots

### 🏠 Homepage – Feedback Form

Shows the user-facing form where feedback is submitted.


![Homepage](screenshots/homepage.png)

### ✅ Thank You Page
Confirmation screen shown after successful feedback submission.

![Thank You](screenshots/thank-you.png)

###  Email Message
Email sent after submitting the feedback

![Email](screenshots/email.png)

### 🛂 Admin Login Page
Secure login page for administrators only.

![Admin Login](screenshots/admin-login.png)

### 📊 Admin Dashboard
View all submitted feedback and update their statuses.

![Admin Dashboard](screenshots/dashboard.png)

when we mark as resolved an email is sent again to remind that their feedback is resolved.

![Email](screenshots/resolved.png)

### 🔍 Check Feedback Status Page
Lets users track the status of their feedback using their name and email.


![Check Status](screenshots/check-status.png)

After login with the submitted name and email.

![feedback Status](screenshots/feedback-status.png)

After mark as resolved in admin dashboard, feedback status is also updated as "Resolved"

![feedback Status](screenshots/feedback-status-resolved.png)


---

## 👨‍💻 Author

**Gaurav Singh** – built with ❤️ and Flask.




