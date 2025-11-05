# 💊 Pillaven SaaS

**Pillaven SaaS** is a team website for the **Pillaven** group, built with **Django**.  
It’s designed to showcase projects, collect client feedback, and manage communication efficiently using Software as a Service (SaaS) principles.

---

## 🚀 Overview

Pillaven SaaS serves as a central platform for:
- 🧩 Displaying our team’s software projects.
- 📨 Collecting user reviews and contact form submissions.
- 🧠 Managing new project uploads via Django’s admin dashboard.
- 💬 Sending support or feedback messages directly to our support email.

All form data is securely stored in the database, and sensitive credentials are managed using environment variables.

---

## 🏗️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default, can be changed)
- **Version Control:** Git & GitHub
- **Email Service:** Django’s built-in email backend (configured with `.env`)

---

## ⚙️ Project Setup

Follow these steps to run **Pillaven SaaS** locally:

### 1️⃣ Clone the Repository
bash
git clone https://github.com/olalekan7857/Pillaven-SaaS.git
cd Pillaven-SaaS



2️⃣ Create and Activate a Virtual Environment
python -m venv .venv
# Activate on Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Database Migrations
python manage.py migrate

5️⃣ Start the Development Server
python manage.py runserver


Then open http://127.0.0.1:8000/
 in your browser.

🔐 Environment Variables

Create a .env file in your project root and add:

EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_generated_app_password


Keep this file private — it’s already listed in .gitignore.

🖼️ Features

📩 Contact Form:
Users can send feedback or inquiries directly to your support email.
All messages are stored in the database for record-keeping.

🧠 Admin Panel Project Management:
Team members can add or manage projects under the Projects section directly from Django Admin.

🌐 Dynamic Website Pages:
Clean and responsive layout for About, Projects, and Contact pages.

🧰 SaaS Model:
Built using scalable SaaS architecture, ensuring easy expansion for new services and client access.

📁 Project Structure
Pillaven-SaaS/
├── pillaven_project/
│   ├── manage.py
│   ├── core/              # Main app
│   ├── templates/
│   ├── static/
│   └── ...
├── requirements.txt
├── .env
├── .gitignore
└── README.md
