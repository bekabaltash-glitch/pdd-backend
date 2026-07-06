from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from app.database import get_db
from app.models.question import Question

router = APIRouter()

@router.get("/random")
def get_random_questions(count: int = Query(default=40), db: Session = Depends(get_db)):
    questions = db.query(Question).order_by(func.random()).limit(count).all()
    return questions

@router.get("/all")
def get_all_questions(
    category: str = Query(default=None),
    db: Session = Depends(get_db)
):
    query = db.query(Question)
    if category:
        query = query.filter(Question.category == category)
    return query.all()

@router.get("/{question_id}")
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        return {"error": "Сұрақ табылмады"}
    return question
