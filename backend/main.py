# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from data.database import get_session
from data.models import TopGainer, TopLoser

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Stock API is live 🔥"}

@app.get("/top-gainers")
def get_top_gainers(db: Session = Depends(get_session)):
    return db.query(TopGainer).all()

@app.get("/top-losers")
def get_top_losers(db: Session = Depends(get_session)):
    return db.query(TopLoser).all()
