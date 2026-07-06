from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models.user import User
import random

router = APIRouter()

# Mock SMS codes storage
sms_codes = {}

class RegisterRequest(BaseModel):
    phone_number: str
    name: str

class LoginRequest(BaseModel):
    phone_number: str

class VerifyRequest(BaseModel):
    phone_number: str
    code: str

@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.phone_number == data.phone_number).first()
    if existing:
        raise HTTPException(status_code=400, detail="Пайдаланушы тіркелген")
    
    user = User(phone_number=data.phone_number, name=data.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    
    # Mock SMS: send code
    code = str(random.randint(1000, 9999))
    sms_codes[data.phone_number] = code
    print(f"SMS code for {data.phone_number}: {code}")  # In prod: real SMS
    
    return {"message": "SMS жіберілді", "user_id": user.id}

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone_number == data.phone_number).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пайдаланушы табылмады")
    
    code = str(random.randint(1000, 9999))
    sms_codes[data.phone_number] = code
    print(f"SMS code for {data.phone_number}: {code}")
    
    return {"message": "SMS жіберілді"}

@router.post("/verify-sms")
def verify_sms(data: VerifyRequest, db: Session = Depends(get_db)):
    stored_code = sms_codes.get(data.phone_number)
    if not stored_code or stored_code != data.code:
        raise HTTPException(status_code=400, detail="Код қате")
    
    user = db.query(User).filter(User.phone_number == data.phone_number).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пайдаланушы табылмады")
    
    del sms_codes[data.phone_number]
    return {"message": "Кіру сәтті", "user_id": user.id, "name": user.name}
