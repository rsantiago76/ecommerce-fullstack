# 🛒 Full Stack API-Driven E-Commerce (FastAPI + React)

A portfolio-ready full-stack e-commerce app:
- **Backend:** FastAPI + SQLAlchemy (SQLite by default, Postgres via `DATABASE_URL`)
- **Frontend:** React (Vite)
- **Deploy:** Render (Backend = Web Service / Docker, Frontend = Static Site)

## ✅ API Endpoints (MVP)
- `GET /health`
- `GET /products`
- `GET /products/{id}`
- `POST /cart/items` (adds item)
- `GET /cart`
- `POST /checkout/create-session` (Stripe-ready placeholder)
- `GET /docs` (Swagger)

## 🔧 Environment Variables
### Backend (optional for MVP)
- `DATABASE_URL` (optional; defaults to SQLite)
- `STRIPE_SECRET_KEY` (optional for real Stripe; placeholder works without)
- `CORS_ORIGINS` (optional; default `*`)

### Frontend
- `VITE_API_BASE_URL` (e.g. `https://your-api.onrender.com`)

## ▶️ Local Run (Docker Compose)
```bash
docker compose up --build
```
- Frontend: http://localhost:5173
- Backend: http://localhost:8000/docs

## ☁️ Render Deploy (recommended order)
1) Deploy **API** as Web Service (Docker)
2) Deploy **UI** as Static Site
3) Set `VITE_API_BASE_URL` to your API URL and redeploy UI
