# 🚀 FastAPI Docker CI/CD Project

## 📌 Overview

This project is a containerized backend application built using FastAPI and PostgreSQL, with a complete Docker and CI/CD setup.

---

## 🛠 Tech Stack

* FastAPI (Backend API)
* PostgreSQL (Database)
* SQLAlchemy (ORM)
* Docker (Containerization)
* Docker Compose (Multi-container orchestration)
* GitHub Actions (CI/CD Pipeline)

---

## ⚙️ Features

* CRUD APIs for product management
* PostgreSQL integration using SQLAlchemy
* Dockerized application and database
* Inter-container communication using Docker networking
* Automated CI/CD pipeline for Docker image build

---

## 🚀 How to Run Locally

```bash
docker-compose up --build
```

---

## 🌐 API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | /              | Health check      |
| GET    | /products      | Get all products  |
| GET    | /products/{id} | Get product by ID |
| POST   | /products      | Create product    |
| PUT    | /products/{id} | Update product    |
| DELETE | /products/{id} | Delete product    |

---

## 🧠 Learnings

* Docker containerization and networking
* Handling real-world issues like port conflicts and DB readiness
* CI/CD pipeline automation using GitHub Actions

---

## 📂 Project Structure

```
.
├── main.py
├── dbconfig.py
├── db_models.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .github/workflows/
```

---

## 👨‍💻 Author

Divyanshu Shekhar