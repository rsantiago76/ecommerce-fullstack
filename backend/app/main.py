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

# ---------- CORS ----------
raw = (settings.CORS_ORIGINS or "").strip()

def normalize(origin: str) -> str:
    return origin.strip().rstrip("/")

if raw == "" or raw == "*":
    # IMPORTANT: "*" cannot be used with allow_credentials=True
    allow_origins = ["*"]
    allow_credentials = False
else:
    allow_origins = [normalize(o) for o in raw.split(",") if o.strip()]
    allow_credentials = True

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(shop_router)
app.include_router(checkout_router)

