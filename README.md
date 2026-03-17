<div align="center">

# ⚡ furious-flask-aws

**A production-style Flask CRUD application deployed on AWS Elastic Beanstalk with PostgreSQL.**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![AWS](https://img.shields.io/badge/AWS-Elastic%20Beanstalk-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/elasticbeanstalk/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon%20%2F%20RDS-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://neon.tech)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat-square&logo=bootstrap&logoColor=white)](https://getbootstrap.com)

</div>

---

## 📸 Overview

A full-stack **Books CRUD application** built with Flask and SQLAlchemy, styled with Bootstrap 5, and deployed on **AWS Elastic Beanstalk** backed by a PostgreSQL database (Neon for development, AWS RDS for production). Features modal-based forms, flash messaging, and an automated CI/CD pipeline via AWS CodePipeline.

---

> **Development**: Uses [Neon](https://neon.tech) (serverless PostgreSQL) via `.env`  
> **Production**: Uses AWS RDS (private, same VPC as EBS)

---

## ✨ Features

- 📚 **Books CRUD** — Create, Read, Update, Delete books via a clean Bootstrap UI
- 🪟 **Modal forms** — Add and Update via Bootstrap modals (no page reloads)
- ⚡ **Flash messages** — Dismissible alerts for user feedback
- 🗄️ **SQLAlchemy ORM** — Clean model definitions with separate `models.py`
- ☁️ **AWS Elastic Beanstalk** — PaaS deployment with `gunicorn`
- 🔄 **CI/CD Pipeline** — Auto-deploy on every `git push` via AWS CodePipeline
- 🔒 **Private RDS** — Database not exposed to internet (VPC-only access)
- 🌱 **Environment-based config** — `.env` for dev, EBS Environment Properties for prod

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11 + Flask |
| ORM | Flask-SQLAlchemy |
| Database (dev) | PostgreSQL via [Neon](https://neon.tech) |
| Database (prod) | AWS RDS PostgreSQL |
| Frontend | Bootstrap 5.3 + Jinja2 |
| WSGI Server | gunicorn |
| Hosting | AWS Elastic Beanstalk |
| CI/CD | AWS CodePipeline |
| Secrets | `.env` (dev) / EBS Environment Properties (prod) |

---

## 📂 Project Structure

```bash
furious-flask-aws/
│
├── application.py          # EBS entry point (required)
├── app.py                  # Flask app factory + routes
├── models/models.py               # SQLAlchemy models (db + Book)
├── requirements.txt        # Python dependencies
├── .env                    # Local environment variables (not committed)
├── .gitignore
│
└── templates/
    ├── base.html           # Bootstrap CDN + layout
    ├── navbar.html         # Top navbar with Add Book button
    └── index.html          # Book table + modals
```

---

## ⚙️ Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/kkamal11/furious-flask-aws.git
cd furious-flask-aws
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://user:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
SECRET_KEY=your-secret-key-here
```

> Get your Neon connection string from [console.neon.tech](https://console.neon.tech)

### 5. Run the app

```bash
python app.py
```

Visit `http://localhost:5000`

---

## 🗄️ Database Setup

Tables are created automatically on first run via `db.create_all()`.

To seed sample data, use Flask shell:

```bash
flask shell
```

```python
from models.models import db, Book

db.session.add_all([
    Book("Atomic Habits", "James Clear", 19.99),
    Book("Clean Code", "Robert C. Martin", 34.50),
    Book("The Pragmatic Programmer", "Andrew Hunt", 42.00),
])
db.session.commit()
```

---

## ☁️ AWS Deployment

### Prerequisites

- AWS account with Elastic Beanstalk and RDS access
- IAM roles: `aws-elasticbeanstalk-service-role` and `aws-elasticbeanstalk-ec2-role`

### 1. Prepare for deployment

Ensure `application.py` exists (required by EBS):

```python
from app import app
application = app
```

Ensure `requirements.txt` uses `psycopg2` (not `psycopg2-binary`) for production:

```bash
Flask
flask-sqlalchemy
psycopg2
gunicorn
python-dotenv
```

### 2. Create EBS environment

In AWS Console → Elastic Beanstalk:

- Platform: Python
- Upload your project as a `.zip` (select files inside the folder, not the folder itself)

### 3. Set environment variables

In EBS → Configuration → Environment properties:

```bash
DATABASE_URL = postgresql://user:password@rds-endpoint:5432/dbname
SECRET_KEY   = your-production-secret-key
```

### 4. Connect RDS (if using AWS RDS)

---

## 🔄 CI/CD with AWS CodePipeline

Every push to `main` auto-deploys to Elastic Beanstalk.

**Pipeline stages:**

1. **Source** — GitHub (via AWS Connector App) → watches `main` branch
2. **Build** — Skip (not required for Flask)
3. **Deploy** — Elastic Beanstalk environment

```bash
  git push origin main
       ↓
  CodePipeline detects change
       ↓
  Deploys to Elastic Beanstalk
       ↓
  App live in ~3 minutes ✅
```

---

## 📋 Requirements

```bash
Flask
flask-sqlalchemy
psycopg2          # use psycopg2-binary for local dev
gunicorn
python-dotenv
```

Install:

```bash
pip install -r requirements.txt
```

---

## 🧠 What I Learned

- Flask application structure with separated models
- SQLAlchemy ORM for PostgreSQL CRUD operations
- Bootstrap 5 modals for clean UX without page reloads
- Flask flash messaging for user feedback
- AWS Elastic Beanstalk deployment (PaaS)
- VPC security groups — keeping RDS private (not publicly accessible)
- AWS CodePipeline CI/CD with GitHub integration
- Difference between `psycopg2` and `psycopg2-binary` (dev vs prod)
- Environment-based configuration (`.env` local vs EBS Environment Properties)

---

## 🗺️ Roadmap

- [ ] Add pagination with SQLAlchemy
- [ ] Add search / filter functionality
- [ ] Delete confirmation modal
- [ ] Add custom domain + HTTPS (AWS Certificate Manager)
- [ ] Containerise with Docker + ECR + ECS (next level)

---

## 📄 License

This project is for learning purposes. Feel free to fork and extend it.

---

<div align="center">

Built with ☁️ on AWS · Flask · Bootstrap · PostgreSQL

</div>