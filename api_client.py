from dotenv import load_dotenv
import os
import requests

# Load the variables from .env -file
load_dotenv()
api_key = os.getenv("API_KEY")


def fetch_data():
    # API-request
    url = "https://data.fingrid.fi/api/datasets/124/data?startTime=2026-02-09T00:00:00Z&endTime=2026-02-09T01:00:00Z&format=json"
    headers = {"x-api-key": api_key}

    response = requests.get(url, headers=headers)
    data = response.json()

    print(data)