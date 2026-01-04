from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .settings import settings
from .db import engine, Base, SessionLocal
from .seed import seed_products
from .routers.shop import router as shop_router
from .routers.checkout import router as checkout_router

app = FastAPI(title="E-Commerce API", version="1.0.0")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    try:
        seed_products(db)
    finally:
        db.close()

# ---- CORS (Render-safe) ----
origins_raw = (settings.CORS_ORIGINS or "").strip()

if not origins_raw:
    origins = ["https://ecommerce-ui-5hvm.onrender.com"]
else:
    origins = [o.strip().rstrip("/") for o in origins_raw.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ----------------------------

@app.get("/debug/headers")
def debug_headers(request: Request):
    return {
        "origin": request.headers.get("origin"),
        "cors_origins_env": settings.CORS_ORIGINS,
    }

@app.get("/health")
def health():
    return {"status": "ok"}



