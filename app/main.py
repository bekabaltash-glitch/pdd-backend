from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, questions, exam, stats
from app.database import create_tables

app = FastAPI(title="PDD Kazakhstan API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(questions.router, prefix="/questions", tags=["Questions"])
app.include_router(exam.router, prefix="/exam", tags=["Exam"])
app.include_router(stats.router, prefix="/stats", tags=["Stats"])

@app.on_event("startup")
async def startup():
    create_tables()

@app.get("/")
def root():
    return {"message": "PDD Kazakhstan API is running"}
