# Webinar Booking Platform 🎥

A Django-based web application for organizing and booking webinars with Google Meet integration.

## 🚀 Features

- 🔐 User authentication (signup, login, logout)
- 🎫 Webinar booking and cancellation
- 🗓 User dashboard displaying all booked webinars
- 📧 Email notifications for booking confirmation
- 🔗 Google Meet integration for live webinar links
- 🛠 Admin panel to create and manage webinars
- 🔒 Environment variables for secure credentials
- ☁️ Hosted on GitHub

## 🛠 Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, Bootstrap (custom theme)
- **Database**: SQLite (can be switched to PostgreSQL/MySQL)
- **External Services**: Google Meet (manual link), Gmail SMTP
- **Version Control**: Git & GitHub

## 🗂 Folder Structure


webinar_platform/
├── webinars/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
├── templates/
│ ├── base.html
│ ├── dashboard.html
├── static/
│ ├── webinar_images/
│ ├── css/
│ ├── js/
├── .env.example
├── manage.py


## 📦 Environment Setup

1. Clone the repo:
    ```
    git clone https://github.com/your-username/Webinar-Booking-Platform.git
    cd Webinar-Booking-Platform
    ```

2. Create a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Create a `.env` file from `.env.example` and fill in your credentials.

5. Run the development server:
    ```
    python manage.py runserver
    ```


## 📌 Note

This project is under active development. More features like Razorpay integration, automated Google Meet generation, and webinar QR scan will be added soon.

---


