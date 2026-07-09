import pandas as pd
import requests
from bs4 import BeautifulSoup

KEYWORDS = [
    "safe deposit",
    "safe deposit box",
    "tangible property",
    "auction",
    "vault",
    "jewelry",
    "gold",
    "silver",
    "coin"
]

states = pd.read_csv("states.csv")

for _, row in states.iterrows():
    state = row["State"]
    url = row["Website"]

    print(f"Checking {state}...")

    try:
        r = requests.get(url, timeout=20)
        soup = BeautifulSoup(r.text, "lxml")
        text = soup.get_text(" ", strip=True).lower()

        matches = [k for k in KEYWORDS if k in text]

        if matches:
            print(f"FOUND: {state}")
            print(matches)
            print(url)
            print("-" * 40)

    except Exception as e:
        print(f"Error checking {state}: {e}")
