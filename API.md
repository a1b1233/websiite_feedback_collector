# 📚 API Documentation – Feedback Collector Web App

## 🧠 Overview

This application allows users to submit feedback and lets the admin manage and update feedback status via a dashboard. It includes email notifications for both submission and resolution.

## 📬 API Endpoints

### 📌 GET /

Description: Home page that renders the feedback form (index.html).

Response: HTML content

### 📌 POST /submit-feedback

Description: Handles feedback form submission, saves it to the database, and sends an email to the user.

Request Body (form-urlencoded):
| Field      | Type   | Required | Description             |
| ---------- | ------ | -------- | ----------------------- |
| `name`     | string | ✅        | User's name             |
| `email`    | string | ✅        | User's email            |
| `rating`   | string | ✅        | User rating (e.g., 5/5) |
| `feedback` | string | ✅        | Feedback text           |


Response: Redirects to /thank-you

Email Sent: Yes, to the user thanking them for their feedback.

### 📌 GET /thank-you

Description: Shows a thank you message after successful feedback submission.

Response: HTML content (thank_you.html)

### 📌 GET /return-home

Description: Redirects the user back to the home page (/).

### 📌 GET /check-status

Description: Renders the form to check submitted feedback status.

Response: HTML page (check_status.html)

### 📌 POST /check-feedback

Description: Returns all feedback entries that match a given name and email.

Request Body (form-urlencoded):

| Field   | Type   | Required | Description  |
| ------- | ------ | -------- | ------------ |
| `name`  | string | ✅        | User's name  |
| `email` | string | ✅        | User's email |


Response: Renders feedback_status.html showing all matched feedbacks or "No Feedback Found" if none.

### 📌 GET /admin-login

Description: Displays the admin login page.

Response: HTML content (admin_login.html)

### 📌 POST /admin-login

Description: Authenticates the admin with static credentials.

Request Body (form-urlencoded):

| Field      | Type   | Required | Value                 |
| ---------- | ------ | -------- | --------------------- |
| `email`    | string | ✅        | `gs7august@gmail.com` |
| `password` | string | ✅        | `8052566305`          |


Response: Redirects to /admin-dashboard on success. Shows alert on failure (handled via JS).

### 📌 GET /admin-dashboard

Description: Displays all feedback entries in a table format.

Response: HTML content showing a list of feedback entries with status update form.

### 📌 POST /update-status/<id>

Description: Updates the status of a specific feedback entry (by id) and sends an email to the user.

Path Param:

id (integer): ID of the feedback entry

Request Body (form-urlencoded):

| Field    | Type   | Required | Description         |
| -------- | ------ | -------- | ------------------- |
| `status` | string | ✅        | New feedback status |


Response: Redirects back to /admin-dashboard

Email Sent: Yes, to notify the user of the updated status.

## 📦 Models

Feedback
| Field      | Type   | Description               |
| ---------- | ------ | ------------------------- |
| `id`       | int    | Primary Key               |
| `name`     | string | User's name               |
| `email`    | string | User's email              |
| `rating`   | string | Rating value              |
| `feedback` | text   | Feedback content          |
| `status`   | string | "Not Resolved" by default |


## 📤 Email Integration

### SMTP Configuration

- SMTP Host: smtp.gmail.com

- Port: 587

- TLS: Enabled

- Email: gs7august2005@gmail.com

- Password: App Password (**** **** **** ****)

Emails are sent during:

- Feedback submission

- Feedback status update

## 🛡 Authentication
- Admin credentials are hardcoded (for demo purposes):

  - Email: gs7august@gmail.com

  - Password: 8052566305

- No session or token-based authentication used.

## ✅ Status Codes

| Status Code | Description                          |
| ----------- | ------------------------------------ |
| `200`       | OK / Render HTML                     |
| `302`       | Redirect (e.g., login, thank you)    |
| `400`       | Form validation failure (JS handled) |
| `500`       | Server error (email fail, DB issues) |
