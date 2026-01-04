from sqlalchemy.orm import Session
from . import models

def seed_products(db: Session):
    if db.query(models.Product).count() > 0:
        return

    products = [
        models.Product(
            sku="TSHIRT-001",
            name="Zero-Trust T-Shirt",
            description="Soft tee with a security mindset. (Demo product)",
            price=24.99,
            image_url="https://picsum.photos/seed/ztshirt/640/480",
        ),
        models.Product(
            sku="MUG-001",
            name="Coffee Mug (Home Brew)",
            description="A mug for late-night debugging sessions. (Demo product)",
            price=14.99,
            image_url="https://picsum.photos/seed/mug/640/480",
        ),
        models.Product(
            sku="STICKER-001",
            name="DevSecOps Sticker Pack",
            description="Proudly slap these on your laptop. (Demo product)",
            price=9.99,
            image_url="https://picsum.photos/seed/stickers/640/480",
        ),
    ]
    db.add_all(products)
    db.commit()
