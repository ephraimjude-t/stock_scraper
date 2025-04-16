import requests
from bs4 import BeautifulSoup
import json
import os
from data.database import SessionLocal, Base, get_session
from data.models import TopGainer, TopLoser

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
base_urls = {
    "gainers": "https://finance.yahoo.com/markets/stocks/gainers/",
    "losers": "https://finance.yahoo.com/markets/stocks/losers/"
}

def top_gainers():
    try:
        response = requests.get(base_urls["gainers"], headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')[1:] if table else []

        data = []
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 4:
                data.append({
                    'symbol': cols[0].text.strip(),
                    'price': cols[1].text.strip(),
                    'change': cols[2].text.strip(),
                    'percent_change': cols[3].text.strip()
                })

        return data

    except Exception as e:
        print(f"[ERROR] Failed to fetch top gainers data: {e}")
        return []

def top_losers():
    try:
        response = requests.get(base_urls["losers"], headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')[1:] if table else []

        data = []
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 4:
                data.append({
                    'symbol': cols[0].text.strip(),
                    'price': cols[1].text.strip(),
                    'change': cols[2].text.strip(),
                    'percent_change': cols[3].text.strip()
                })

        return data

    except Exception as e:
        print(f"[ERROR] Failed to fetch top losers data: {e}")
        return []

def save_to_json(data):
    # Make sure data directory exists
    os.makedirs("data", exist_ok=True)

    output_file = os.path.join("data", "top_movers.json")
    try:
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"[INFO] Top movers data saved to {output_file}")
    except Exception as e:
        print(f"[ERROR] Failed to save JSON: {e}")

def save_top_gainers(top_gainers):
    from data.database import SessionLocal, Base, get_session
    db = SessionLocal()
    try:
        for gainer_data in top_gainers:
            gainer = TopGainer(
                symbol=gainer_data['symbol'],
                price=gainer_data['price'],
                change=gainer_data['change'],
                percent_change=gainer_data['percent_change']
            )
            db.add(gainer)
        db.commit()
    except Exception as e:
        print(f"[ERROR] Failed to save top gainers to database: {e}")
    finally:
        db.close()

def save_top_losers(top_losers):
    from data.database import SessionLocal, Base, get_session

    db = SessionLocal()
    try:
        for loser_data in top_losers:
            loser = TopLoser(
                symbol=loser_data['symbol'],
                price=loser_data['price'],
                change=loser_data['change'],
                percent_change=loser_data['percent_change']
            )
            db.add(loser)
        db.commit()
    except Exception as e:
        print(f"[ERROR] Failed to save top losers to database: {e}")
    finally:
        db.close()

def main():
    # Fetch data
    gainers_data = top_gainers()
    losers_data = top_losers()

    # Save to database
    save_top_gainers(gainers_data)
    save_top_losers(losers_data)

    # Optionally save to JSON
    save_to_json({
        "gainers": gainers_data,
        "losers": losers_data
    })

if __name__ == "__main__":
    main()
