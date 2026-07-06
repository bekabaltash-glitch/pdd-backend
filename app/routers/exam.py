from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from pydantic import BaseModel
from typing import Dict
from datetime import datetime
from app.database import get_db
from app.models.exam import ExamSession
from app.models.question import Question
from app.models.user import User

router = APIRouter()

class StartExamRequest(BaseModel):
    user_id: int

class SubmitExamRequest(BaseModel):
    exam_id: int
    user_id: int
    answers: Dict[str, str]  # {question_id: selected_answer}

@router.post("/start")
def start_exam(data: StartExamRequest, db: Session = Depends(get_db)):
    questions = db.query(Question).order_by(func.random()).limit(40).all()
    
    exam = ExamSession(user_id=data.user_id, total_questions=len(questions))
    db.add(exam)
    db.commit()
    db.refresh(exam)
    
    return {
        "exam_id": exam.id,
        "questions": questions,
        "time_limit_minutes": 40
    }

@router.post("/submit")
def submit_exam(data: SubmitExamRequest, db: Session = Depends(get_db)):
    exam = db.query(ExamSession).filter(ExamSession.id == data.exam_id).first()
    if not exam:
        return {"error": "Емтихан табылмады"}
    
    # Calculate score
    score = 0
    results = {}
    for question_id, selected in data.answers.items():
        question = db.query(Question).filter(Question.id == int(question_id)).first()
        if question:
            is_correct = question.correct_answer == selected
            if is_correct:
                score += 1
            results[question_id] = {
                "selected": selected,
                "correct": question.correct_answer,
                "is_correct": is_correct
            }
    
    passed = score >= 28  # 70% to pass (28/40)
    
    exam.score = score
    exam.passed = passed
    exam.finished_at = datetime.now()
    exam.answers = data.answers
    db.commit()
    
    # Update user stats
    user = db.query(User).filter(User.id == data.user_id).first()
    if user:
        user.score += score
        user.exams_taken += 1
        db.commit()
    
    return {
        "score": score,
        "total": exam.total_questions,
        "passed": passed,
        "percentage": round(score / exam.total_questions * 100),
        "results": results
    }

@router.get("/history/{user_id}")
def get_exam_history(user_id: int, db: Session = Depends(get_db)):
    exams = db.query(ExamSession).filter(ExamSession.user_id == user_id).order_by(ExamSession.started_at.desc()).all()
    return exams
