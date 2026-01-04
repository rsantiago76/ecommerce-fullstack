from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_db
from .. import schemas
from ..settings import settings

router = APIRouter(prefix="/checkout", tags=["checkout"])

@router.post("/create-session", response_model=schemas.CheckoutOut)
def create_session(db: Session = Depends(get_db)):
    if settings.STRIPE_SECRET_KEY:
        return schemas.CheckoutOut(
            mode="stripe-configured",
            checkout_url=None,
            message="Stripe key is set. Next step: create a real Checkout Session with line items."
        )

    return schemas.CheckoutOut(
        mode="demo",
        checkout_url=None,
        message="Demo checkout: set STRIPE_SECRET_KEY to enable Stripe session creation."
    )
