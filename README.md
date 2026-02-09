# Open Data App
This application fetches electricity consumption data from the Fingrid Open Data API. The user can select a time range, and the data is presented in a chart.
## How to obtain the API key
1. Go to the Fingrid Open Data Portal: [https://data.fingrid.fi/](https://data.fingrid.fi/)
2. Create an account or log in with an existing account.
3. Go to Developer portal via the **Control panel**.
4. Sign in to the developer portal
5. Go to **Products** where you can subscribe to the API
6. Choose Open Data starter, write a name for subscription and then press the Subscribe button.

## How to configure the API key
The application reads the API key from a .env file.
1. In the project folder, create an .env file.
2. Add the following line: API_KEY=your_api_key_here
