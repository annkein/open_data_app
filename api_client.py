from dotenv import load_dotenv
import os
import requests

# Load the variables from .env -file
load_dotenv()
api_key = os.getenv("API_KEY")

# Only one dataset is in use
DATASET_ID = 124
BASE_URL = "https://data.fingrid.fi/api/datasets"

def fetch_data():
    """
    Fetch data from Fingrid Open Data API.
    """
    # API-request
    url = f"{BASE_URL}/{DATASET_ID}/data?startTime=2026-02-09T00:00:00Z&endTime=2026-02-09T01:00:00Z&format=json"
    headers = {"x-api-key": api_key}

    response = requests.get(url, headers=headers)

    # Check for errors in response
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
    
    data = response.json()

    print(data)