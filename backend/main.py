from fastapi import FastAPI
from data.top_movers import get_losers_gainers
from data.scheduler import scheduler
import os
import json

app = FastAPI()

@app.on_event("startup")
def start_scheduler():
    print("[INFO] Starting scheduler...")
    scheduler.start()

@app.get("/")
def read_root():
    return {"Welcome": "to the app!"}

@app.get("/top_movers")
def get_top_movers():
    output_file = os.path.join("data", "top_movers.json")
    if not os.path.exists(output_file):
        return {"error": "Data file not found. Please run the data fetching script."}
    with open(output_file, 'r') as f:
        data = json.load(f)
    return data

@app.get("/fetch_top_movers")
def fetch_top_movers():
    data = get_losers_gainers()
    return {"message": "Top movers data fetched successfully.", "data": data}
