import requests
from bs4 import BeautifulSoup
import json
import os
from sqlalchemy.orm import Session
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
            if len(cols) >= 5:  # Ensure at least the first 5 columns are present
                data.append({
                    'symbol': cols[0].text.strip(),
                    'name': cols[1].text.strip(),
                    'price': cols[2].text.strip(),
                    'change': cols[3].text.strip(),
                    'percent_change': cols[4].text.strip()
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
            if len(cols) >= 10:  # Ensure at least the first 5 columns are present
                data.append({
                    'symbol': cols[0].text.strip(),
                    'name': cols[1].text.strip(),
                    'price': cols[2].text.strip(),
                    'change': cols[4].text.strip(),
                    'percent_change': cols[5].text.strip()
                })

        return data

    except Exception as e:
        print(f"[ERROR] Failed to fetch top losers data: {e}")
        return []

#export to json
def export_top_gainers():
    gainers_data = top_gainers()
    with open('top_gainers.json', 'w') as json_file:
        json.dump(gainers_data, json_file)

def export_top_losers():
    losers_data = top_losers()
    with open('top_losers.json', 'w') as json_file:
        json.dump(losers_data, json_file)

if __name__ == "__main__":
    export_top_gainers()
    export_top_losers()