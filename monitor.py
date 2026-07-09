import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

KEYWORDS = [
    "safe deposit",
    "safe deposit box",
    "tangible property",
    "auction",
    "vault",
    "contents",
    "jewelry",
    "coins",
    "gold",
    "silver",
]

with open("states.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print(f"\nUS Property Monitor")
    print(f"Scan Time: {datetime.utcnow()} UTC\n")

    for row in reader:
        state = row["State"]
        url = row["Website"]

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(" ", strip=True).lower()

            matches = [k for k in KEYWORDS if k in text]

            if matches:
                print("=" * 60)
                print(f"STATE: {state}")
                print(f"WEBSITE: {url}")
                print("MATCHES:")
                for m in matches:
                    print(f" - {m}")

        except Exception as e:
            print(f"{state}: {e}")
