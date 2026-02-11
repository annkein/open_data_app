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
    Fetch electricity consumption data from Fingrid Open Data
    API's dataset 124 (Finnish electricity consumption in MW) 
    for a user-specified time range. The data is returned as a 
    cleaned and sorted pandas DataFrame, with start and 
    end timestamps converted to datetime objects and values rounded.

    :param (str) start_time: Start time in ISO 8601 format, e.g. "2026-02-09T00:00:00Z"
    :param (str) end_time: End time in ISO 8601 format, e.g. "2026-02-09T00:00:00Z"

    :return: pd.DataFrame, with columns startTime, endTime and Electricity Consumption (MW).
    """

    if not API_KEY:
        raise RuntimeError("API_KEY is missing. Check your .env file.")

    # Set the url, headers, and parameters for the API request
    url = f"{BASE_URL}/{DATASET_ID}/data"
    headers = {"x-api-key": API_KEY}
    params = {
        "startTime": start_time,
        "endTime": end_time,
        "format": "json",
        "pageSize": 5000    # For getting larger time frames in the data
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

    # Convert times
    df["startTime"] = pd.to_datetime(df["startTime"])
    df["endTime"] = pd.to_datetime(df["endTime"])

    # Rename value column to make clearer
    df = df.rename(columns={
        "value": "Electricity consumption (MW)"
    })

    # Sort by time and keep relevant columns
    df = df.sort_values("startTime").reset_index(drop=True)
    df = df[["startTime", "endTime", "Electricity consumption (MW)"]]

    # Round values for nicer output
    df["Electricity consumption (MW)"] = df["Electricity consumption (MW)"].round(1)

    return df
