from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from ..db import get_db
from .. import models, schemas
from ..auth import get_current_user_id

router = APIRouter(tags=["shop"])

@router.get("/products", response_model=list[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    products = db.execute(select(models.Product).order_by(models.Product.id.asc())).scalars().all()
    return [schemas.ProductOut(**p.__dict__) for p in products]

@router.get("/products/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    p = db.get(models.Product, product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    return schemas.ProductOut(**p.__dict__)

@router.post("/cart/items", response_model=schemas.CartOut)
def add_to_cart(
    payload: schemas.CartItemIn,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
):
    p = db.get(models.Product, payload.product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")

    existing = (
        db.query(models.CartItem)
        .filter(models.CartItem.user_id == user_id, models.CartItem.product_id == payload.product_id)
        .first()
    )

    if existing:
        existing.quantity += payload.quantity
        db.add(existing)
    else:
        db.add(models.CartItem(user_id=user_id, product_id=payload.product_id, quantity=payload.quantity))

    db.commit()
    return _cart(db, user_id)

@router.get("/cart", response_model=schemas.CartOut)
def get_cart(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
):
    return _cart(db, user_id)

@router.delete("/cart", response_model=schemas.CartOut)
def clear_cart(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
):
    db.query(models.CartItem).filter(models.CartItem.user_id == user_id).delete()
    db.commit()
    return _cart(db, user_id)

def _cart(db: Session, user_id: int) -> schemas.CartOut:
    items = (
        db.query(models.CartItem)
        .filter(models.CartItem.user_id == user_id)
        .order_by(models.CartItem.created_at.desc())
        .all()
    )

    out_items = []
    subtotal = 0.0
    for it in items:
        prod = it.product
        prod_out = schemas.ProductOut(
            id=prod.id, sku=prod.sku, name=prod.name, description=prod.description,
            price=prod.price, image_url=prod.image_url
        )
        out_items.append(schemas.CartItemOut(
            id=it.id, product_id=it.product_id, quantity=it.quantity, product=prod_out
        ))
        subtotal += prod.price * it.quantity

    return schemas.CartOut(items=out_items, subtotal=round(subtotal, 2))
