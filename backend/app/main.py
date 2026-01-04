from fastapi import FastAPI
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

if origins_raw == "*" or origins_raw == "":
    # Wildcard mode (public API) — must NOT use credentials with "*"
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    # Explicit origin(s) — credentials are OK
    origins = [o.strip() for o in origins_raw.split(",") if o.strip()]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
# ----------------------------


@app.get("/health")
def health():
    return {"status": "ok"}


