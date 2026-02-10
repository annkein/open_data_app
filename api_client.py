from dotenv import load_dotenv
import os
import requests
import pandas

# Load the variables from .env -file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Only one dataset is in use
DATASET_ID = 124
BASE_URL = "https://data.fingrid.fi/api/datasets"

def fetch_data(start_time: str, end_time: str):
    """
    Fetch data from Fingrid Open Data API.

    Parameters:
        start_time (str): Start time in ISO 8601 format, e.g. "2026-02-09T00:00:00Z"
        end_time (str): End time in ISO 8601 format
    """

    # Set the url, headers, and parameters for the API request
    url = f"{BASE_URL}/{DATASET_ID}/data"
    headers = {"x-api-key": API_KEY}
    params = {
        "startTime": start_time,
        "endTime": end_time,
        "format": "json"
    }

    response = requests.get(url, headers=headers, params=params)

    # Check for errors in response
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
    
    data = response.json()

    # Convert data into DataFrame
    df = pandas.DataFrame(data["data"])
    df['startTime'] = pandas.to_datetime(df['startTime'])
    df['endTime'] = pandas.to_datetime(df['endTime'])

    return df