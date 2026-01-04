# 🛒 Full Stack API-Driven E-Commerce Backend + UI

This repo contains a portfolio-ready full-stack e-commerce app.

- **Frontend (React/Vite):** `frontend/` (Render Static Site)
- **Backend (FastAPI):** `backend/` (Render Web Service / Docker)

## Architecture
- React UI calls the FastAPI API over HTTPS
- API stores products + cart items in DB (SQLite by default; Postgres supported via `DATABASE_URL`)
- Checkout endpoint is Stripe-ready (safe placeholder)

## Local Run
```bash
docker compose up --build
```

## Deploy to Render
Recommended order:
1) Deploy **API** (Web Service, Docker) using `backend/Dockerfile`
2) Deploy **UI** (Static Site) from `frontend/`
3) Set `VITE_API_BASE_URL` in UI to your API URL and redeploy

## Live URLs
- Frontend: <ADD_UI_URL>
- Backend/API: <ADD_API_URL>
- API Docs: <ADD_API_URL>/docs
