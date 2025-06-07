from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.db.session import SessionLocal
from app.schemas.user import UserCreate
from app.crud.user import get_user_by_email
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/registration")
def registration(payload: UserCreate, db: Session = Depends(get_db)):
    email = payload.email.lower()

    if get_user_by_email(db, email):
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=email,
        first_name=payload.first_name,
        last_name=payload.last_name
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "Registration successful",
        "user": {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
    }