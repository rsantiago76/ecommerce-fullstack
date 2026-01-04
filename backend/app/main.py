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

origins = [o.strip() for o in settings.CORS_ORIGINS.split(",")] if settings.CORS_ORIGINS else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(shop_router)
app.include_router(checkout_router)
