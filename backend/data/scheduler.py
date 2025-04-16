from apscheduler.schedulers.background import BackgroundScheduler
from .top_movers import get_losers_gainers

def job():
    print("[INFO] Fetching top movers...")
    get_losers_gainers()

scheduler = BackgroundScheduler()
scheduler.add_job(job, 'cron', hour='0,12')  # Every 12 hours
