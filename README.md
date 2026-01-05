⚡️ Full-Stack E-Commerce Demo

React UI · FastAPI Backend · Docker · Render Cloud

A production-style, API-driven e-commerce demo showcasing a modern React frontend communicating with a FastAPI backend, fully deployed on Render using a Static Site + Dockerized Web Service architecture.

This project is designed as a portfolio reference for:

API-first design

Full-stack cloud deployment

Real-world CORS, env vars, Docker, and Render workflows

🚀 Live Demo

Frontend (React UI)
👉 https://ecommerce-ui-5hvm.onrender.com/

Backend API (FastAPI)
👉 https://ecommerce-api-6bni.onrender.com

Interactive API Docs (Swagger)
👉 https://ecommerce-api-6bni.onrender.com/docs

🧩 Architecture
<img src="https://github.com/user-attachments/assets/3f74f430-e3f2-4ffb-9546-9380d45277b6" alt="Architecture Diagram" width="900" />

Flow

React UI (Static Site) runs in the browser

UI calls FastAPI endpoints over HTTPS

FastAPI exposes product, cart, and checkout APIs

Backend runs as a Dockerized Web Service on Render

Render hosts both the Static Site and API

🛒 Features

📦 Product catalog API

🛍️ Demo cart functionality

💳 Stripe-ready checkout endpoint (safe placeholder)

🔐 CORS-safe cross-origin API access

📊 API documentation via Swagger

☁️ Cloud deployment with Render

🐳 Dockerized backend

🧾 Tech Stack
Frontend

React (hooks + functional components)

Vite (fast dev & build tooling)

Fetch API

Environment-based API configuration

Backend

FastAPI

SQLAlchemy ORM

SQLite (default)
→ PostgreSQL supported via DATABASE_URL

JWT-ready auth scaffolding

Stripe-ready checkout endpoint

Infrastructure & Deployment

Render Static Site (Frontend)

Render Web Service (Docker) (Backend)

Docker

Environment variables via Render Dashboard

🧪 Local Development
Run Everything with Docker (Recommended)
docker compose up --build

Backend (Manual)
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

Frontend (Manual)
cd frontend
npm install
npm run dev


Create frontend/.env:

VITE_API_BASE_URL=http://localhost:8000

☁️ How to Deploy on Render (Step-by-Step)
1️⃣ Deploy Backend (Web Service)

Service Type: Web Service

Environment: Docker

Root Directory: backend

Dockerfile: backend/Dockerfile

Health Check Path: /health

Environment Variables

CORS_ORIGINS=https://ecommerce-ui-5hvm.onrender.com
DATABASE_URL=<optional Postgres URL>
STRIPE_SECRET_KEY=<optional>


Deploy 🚀

2️⃣ Deploy Frontend (Static Site)

Service Type: Static Site

Root Directory: frontend

Build Command: npm install && npm run build

Publish Directory: dist

Environment Variable

VITE_API_BASE_URL=https://ecommerce-api-6bni.onrender.com


Deploy 🚀

🔐 Security & Notes

No secrets are committed

Checkout endpoint is demo-only

Designed for learning, demos, and portfolio use

Easily extensible for real auth, payments, and users

📌 Pin-Worthy GitHub Description

Short Description

Full-stack e-commerce demo with React, FastAPI, Docker, and Render — showcasing API-driven UI architecture and cloud deployment.

Tags

react fastapi docker render fullstack ecommerce api portfolio cloud-deployment

⭐ Why This Project Matters

This repo demonstrates:

Real API ↔ UI integration

Cross-origin security handling (CORS)

Docker-based cloud deployment

Clean separation of frontend and backend concerns

Practical DevSecOps-ready structure
