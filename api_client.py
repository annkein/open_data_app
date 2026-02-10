from dotenv import load_dotenv
import os
import requests
import pandas as pd

# Load the variables from .env -file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Since only one dataset is in use, set the id of it as a constant
DATASET_ID = 124
BASE_URL = "https://data.fingrid.fi/api/datasets"

def fetch_data(start_time: str, end_time: str) -> pd.DataFrame:
    """
    Fetch data from Fingrid Open Data API.

    Parameters:
        start_time (str): Start time in ISO 8601 format, e.g. "2026-02-09T00:00:00Z"
        end_time (str): End time in ISO 8601 format
    """

    if not API_KEY:
        raise RuntimeError("API_KEY is missing. Check your .env file.")

    # Set the url, headers, and parameters for the API request
    url = f"{BASE_URL}/{DATASET_ID}/data"
    headers = {"x-api-key": API_KEY}
    params = {
        "startTime": start_time,
        "endTime": end_time,
        "format": "json"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Network or API error: {e}")

    json_data = response.json()

    # Check if data exists (All data from Fingrid Open Data used in 
    # this program is under the key word "data")
    if "data" not in json_data or not json_data["data"]:
        raise ValueError("No data returned for the given time range.")

    # Convert data into DataFrame
    df = pd.DataFrame(json_data["data"])
    df['startTime'] = pd.to_datetime(df['startTime'])
    df['endTime'] = pd.to_datetime(df['endTime'])

    return df