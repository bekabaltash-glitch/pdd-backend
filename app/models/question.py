from sqlalchemy import Column, Integer, String
from app.database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text_kz = Column(String)
    text_ru = Column(String)
    option_a_kz = Column(String)
    option_b_kz = Column(String)
    option_c_kz = Column(String)
    option_d_kz = Column(String)
    option_a_ru = Column(String)
    option_b_ru = Column(String)
    option_c_ru = Column(String)
    option_d_ru = Column(String)
    correct_answer = Column(String)  # a/b/c/d
    category = Column(String)  # signs/markings/rules/first_aid
    image_url = Column(String, nullable=True)
    explanation_kz = Column(String, nullable=True)
    explanation_ru = Column(String, nullable=True)
