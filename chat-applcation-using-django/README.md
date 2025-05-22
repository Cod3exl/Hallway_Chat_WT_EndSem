# Hallway-Chat

A modern, user-friendly chat platform built with Django and Material Design 3. This project demonstrates how to create a real-time(ish) chat application with user authentication, contact management, chat invites, and a beautiful, responsive interface.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [How the App Works](#how-the-app-works)
- [Detailed File/Folder Explanations](#detailed-filefolder-explanations)
- [How Real-Time Chat Works](#how-real-time-chat-works)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Project Overview

**Hallway-Chat** is a web-based chat application where users can:

- Register and log in securely
- Add other users as contacts (with an invite/accept system)
- Chat in real-time (using AJAX polling)
- Enjoy a clean, modern, and responsive UI

This project is designed to be easy to understand, even for those new to Django or web development.

---

## Features

- **User Registration & Login:** Secure authentication using Django's built-in system.
- **Profile Avatars:** Each user can have a profile picture (avatar).
- **Contact Management:** Add contacts by username, with an invite/accept/decline workflow.
- **Real-Time Messaging:** Messages appear automatically (AJAX polling every 2 seconds).
- **Responsive Design:** Works on desktop, tablet, and mobile.
- **Material Design 3 UI:** Modern look and feel with smooth interactions.
- **No intrusive popups:** The chat window remains fixed and clean.

---

## Project Structure

```
chat_platform/
├── chat_platform/          # Main Django project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chat/                   # Chat application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── signals.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       └── chat/
│           └── chat.html
├── static/
│   ├── css/
│   │   ├── material.css
│   │   └── styles.css
│   ├── js/
│   │   ├── chat.js
│   │   └── material.js
│   └── images/
│       └── favicon.ico
├── db.sqlite3              # SQLite database file
└── manage.py
```

---

## Technologies Used

- **Python 3**
- **Django 5.x** (web framework)
- **SQLite** (default database)
- **HTML5, CSS3, JavaScript**
- **Material Design 3** (for UI)
- **AJAX (fetch API)** for real-time message polling

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd chat-applcation-using-django
```

### 2. Install Dependencies

Make sure you have Python 3 and pip installed.

```bash
pip install django pillow
```

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a Superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## How the App Works

### User Flow

1. **Register:** New users sign up with a username and password.
2. **Login:** Users log in to access the chat platform.
3. **Add Contacts:** Use the "+" button to send an invite to another user by username.
4. **Accept/Decline Invites:** Recipients see pending invites and can accept or decline.
5. **Chat:** Once contacts, users can send messages to each other. Messages appear in real-time.
6. **Profile:** The logged-in user's name and avatar are always visible in the top right.

### Real-Time Messaging

- The chat window polls the server every 2 seconds for new messages using AJAX.
- When a new message is sent or received, it appears instantly in the chat window.
- The chat input box is always fixed at the bottom of the chat area.

---

## Detailed File/Folder Explanations

### Top-Level

- **manage.py:** Django's command-line utility for running the server, migrations, etc.
- **db.sqlite3:** The SQLite database file where all data is stored.
- **static/:** Contains all static files (CSS, JS, images) used by the app.

### `chat_platform/` (Main Project)

- **settings.py:** Main configuration file (database, static files, installed apps, etc).
- **urls.py:** Routes URLs to the correct app/views.
- **asgi.py/wsgi.py:** Entry points for ASGI/WSGI servers (for deployment).

### `chat/` (Chat App)

- **models.py:** Defines the database models:
  - `Profile`: User profile with avatar and status.
  - `Contact`: Represents a contact relationship between users.
  - `Message`: Stores chat messages.
  - `ChatInvite`: Handles pending chat invites.
- **views.py:** Contains all the logic for registration, login, chat, sending messages, managing contacts, and invites.
- **urls.py:** Maps URLs to views for the chat app.
- **signals.py:** Ensures every user has a profile (auto-creates on registration).
- **templates/:**
  - **base.html:** The main layout (header, footer, navigation, user info).
  - **home.html:** The landing page.
  - **auth/login.html, auth/register.html:** Login and registration forms.
  - **chat/chat.html:** The main chat interface (contacts, chat area, invites).

### `static/`

- **css/material.css:** Material Design 3 base styles.
- **css/styles.css:** Custom styles for layout, chat bubbles, responsiveness, etc.
- **js/material.js:** Handles UI interactions (menus, mobile nav, etc).
- **js/chat.js:** (If present) Handles chat-specific JS (may be merged into chat.html inline script).
- **images/favicon.ico:** The site favicon.

---

## How Real-Time Chat Works (AJAX Polling)

- When a chat is open, JavaScript fetches new messages from the server every 2 seconds.
- The server returns all messages between the two users as JSON.
- The chat window updates automatically if new messages are found.
- This is a simple, reliable way to simulate real-time chat without WebSockets.

---

## Customization

- **Change Colors:** Edit `static/css/styles.css` and `material.css` for your own color palette.
- **Change Logo:** Update the logo text or replace with an image in `base.html`.
- **Add Features:** You can extend the app with group chat, file uploads, emojis, etc.
- **Switch to WebSockets:** For true real-time chat, consider using Django Channels.

---

## Troubleshooting

- **CSRF Errors:** Make sure all forms include `{% csrf_token %}` and you are not blocking cookies.
- **Static Files Not Loading:** Ensure `DEBUG = True` in `settings.py` for local development.
- **Database Issues:** If you change models, always run `makemigrations` and `migrate`.
- **Admin Access:** Visit `/admin` and log in with your superuser account to manage users and data.

---

## License

This project is for educational purposes. You are free to use, modify, and share it as you wish.
