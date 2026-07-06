from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.exam import ExamSession

router = APIRouter()

@router.get("/{user_id}")
def get_stats(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "Пайдаланушы табылмады"}
    
    exams = db.query(ExamSession).filter(ExamSession.user_id == user_id).all()
    passed_exams = [e for e in exams if e.passed]
    
    return {
        "user_id": user_id,
        "name": user.name,
        "total_score": user.score,
        "exams_taken": user.exams_taken,
        "exams_passed": len(passed_exams),
        "pass_rate": round(len(passed_exams) / len(exams) * 100) if exams else 0,
        "average_score": round(sum(e.score for e in exams) / len(exams)) if exams else 0
    }
