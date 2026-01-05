from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from ..db import get_db
from .. import models, schemas

router = APIRouter(tags=["shop"])


@router.get("/products", response_model=list[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    products = (
        db.execute(
            select(models.Product).order_by(models.Product.id.asc())
        )
        .scalars()
        .all()
    )
    return [schemas.ProductOut(**p.__dict__) for p in products]


@router.get("/products/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(models.Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return schemas.ProductOut(**product.__dict__)

