# Electricity Consumption Viewer (Fingrid Open Data)
## Description

This Python application fetches electricity consumption data from the Fingrid Open Data API. The user can select a time range, after which the application retrieves the corresponding electricity consumption data, processes it into a structured format, and presents the results in a readable table in the command line and as a simple line chart visualization.

The application uses dataset **124**, which represents electricity consumption in Finland. The data resolution is 15 minutes, and values are measured in megawatts (MW).

## How to obtain an API key
The Fingrid Open Data page has [more detailed API instructions](https://data.fingrid.fi/en/instructions), but the basic steps are:

1. Go to the Fingrid Open Data Portal: [https://data.fingrid.fi/](https://data.fingrid.fi/)
2. Create an account or log in with an existing account.
3. Go to Developer portal via the **Control panel**.
4. Sign in to the developer portal
5. Go to **Products** where you can subscribe to the API
6. Choose Open Data starter, write a name for subscription and then press the Subscribe button.

## How to configure the API key
The application reads the API key from a `.env` file.
1. In the project folder, create an `.env` file.
2. Add the following line to the `.env` file: `API_KEY=your_api_key_here`

## How to install and run the application
### Installation
Prerequisites are: Python 3.8 or newer and Git.
Then:
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/Scripts/activate`
4. Install required dependencies: `pip install -r requirements.txt`

### Running
1. the application can be run with: `python main.py`
2. After this, the program will ask for a start and end date: `Enter start date (YYYY-MM-DD):`, `Enter end date (YYYY-MM-DD):`

#### Example run and output
`python main.py`
Enter start date (YYY-MM-DD): `2026-01-01`
Enter end date (YYYY-MM-DD): `2026-01-31`

Expected output (with the visual graph that pops up as separate window):

Data preview (first 10 rows):
                startTime                   endTime  Electricity consumption (MW)
2026-01-01 00:00:00+00:00 2026-01-01 00:15:00+00:00                       12173.6
2026-01-01 00:15:00+00:00 2026-01-01 00:30:00+00:00                       12182.1
2026-01-01 00:30:00+00:00 2026-01-01 00:45:00+00:00                       12215.0
2026-01-01 00:45:00+00:00 2026-01-01 01:00:00+00:00                       12299.3
2026-01-01 01:00:00+00:00 2026-01-01 01:15:00+00:00                       12240.4
2026-01-01 01:15:00+00:00 2026-01-01 01:30:00+00:00                       12307.5
2026-01-01 01:30:00+00:00 2026-01-01 01:45:00+00:00                       12327.2
2026-01-01 01:45:00+00:00 2026-01-01 02:00:00+00:00                       12357.8
2026-01-01 02:00:00+00:00 2026-01-01 02:15:00+00:00                       12356.5
2026-01-01 02:15:00+00:00 2026-01-01 02:30:00+00:00                       12365.1

Total rows returned: 2975
Time range in data: 2026-01-01 00:00:00+00:00 -> 2026-01-31 23:30:00+00:00

Summary statistics:
Average consumption: 12891.3 MW
Minimum consumption: 9886.2 MW
Maximum consumption: 15553.1 MW


