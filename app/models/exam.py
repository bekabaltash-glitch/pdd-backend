from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class ExamSession(Base):
    __tablename__ = "exam_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    started_at = Column(DateTime, default=func.now())
    finished_at = Column(DateTime, nullable=True)
    score = Column(Integer, default=0)
    total_questions = Column(Integer, default=40)
    passed = Column(Boolean, default=False)
    answers = Column(JSON, nullable=True)  # {question_id: selected_answer}
