# main.py
from fastapi import FastAPI
from movers import top_gainers, top_losers
import json

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Stock API is live 🔥"}

@app.get("/top-gainers")
# pull from export top_gainers
def get_top_gainers():
    gainers_data = top_gainers()
    return gainers_data
def store_top_gainers_to_json(gainers_data):
    with open('top_gainers.json', 'w') as json_file:
        json.dump(gainers_data, json_file)

@app.get("/top-losers")
def get_top_losers():
    losers_data = top_losers()
    return losers_data
def store_top_losers_to_json(losers_data):
    with open('top_losers.json', 'w') as json_file:
        json.dump(losers_data, json_file)
    