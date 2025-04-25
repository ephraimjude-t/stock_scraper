import requests
from bs4 import BeautifulSoup
import json
import os

# Moved here ⬇️
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
base_urls = {
    "gainers": "https://finance.yahoo.com/markets/stocks/gainers/",
    "losers": "https://finance.yahoo.com/markets/stocks/losers/"
}

def fetch_movers(mover_type):
    try:
        response = requests.get(base_urls[mover_type], headers=headers, timeout=10)
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
        print(f"[ERROR] Failed to fetch top {mover_type} data: {e}")
        return []

def top_gainers():
    return fetch_movers("gainers")

def top_losers():
    return fetch_movers("losers")


# Test the functions
if __name__ == "__main__":
    print("Top Gainers:")
    print(json.dumps(top_gainers(), indent=4))

    print("\nTop Losers:")
    print(json.dumps(top_losers(), indent=4))