import requests
from bs4 import BeautifulSoup
import json
import os

def get_losers_gainers():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    base_urls = {
        "gainers": "https://finance.yahoo.com/markets/stocks/gainers/",
        "losers": "https://finance.yahoo.com/markets/stocks/losers/"
    }

    results = {}

    for label, url in base_urls.items():
        try:
            response = requests.get(url, headers=headers, timeout=10)
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

            results[label] = data

        except Exception as e:
            print(f"[ERROR] Failed to fetch {label} data: {e}")
            results[label] = []

           

    # Make sure data directory exists
    os.makedirs("data", exist_ok=True)

    output_file = os.path.join("data", "top_movers.json")
    try:
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=4)
        print(f"[INFO] Top movers data saved to {output_file}")
    except Exception as e:
        print(f"[ERROR] Failed to save JSON: {e}")

    return results

if __name__ == "__main__":
    data = get_losers_gainers()
    print(json.dumps(data, indent=2))


