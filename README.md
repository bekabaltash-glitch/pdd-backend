# PDD Kazakhstan Backend

## Орнату

```bash
pip install -r requirements.txt
```

## Базаны толтыру (5 үлгі сұрақ)

```bash
python seed.py
```

## Іске қосу

```bash
uvicorn app.main:app --reload
```

## API документация

Браузерде ашу: http://localhost:8000/docs

## Endpoints

- POST /auth/register — тіркелу
- POST /auth/login — кіру
- POST /auth/verify-sms — SMS коды тексеру
- GET /questions/random?count=40 — кездейсоқ сұрақтар
- GET /questions/all — барлық сұрақтар
- POST /exam/start — емтихан бастау
- POST /exam/submit — жауаптар жіберу
- GET /exam/history/{user_id} — тарих
- GET /stats/{user_id} — статистика
