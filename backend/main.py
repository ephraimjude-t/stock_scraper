from movers import top_gainers, top_losers
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
origins = [
    "http://localhost:3000",
    "https://your-production-domain.com",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Stock Movers API!"}

@app.get("/top-gainers")
def get_top_gainers():
    return {"gainers": top_gainers()}


@app.get("/top-losers")
def get_top_losers():
    return {"losers": top_losers()}
