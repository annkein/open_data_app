from api_client import fetch_data

def main():
   start = input("Enter start date (YYYY-MM-DD): ") + "T00:00:00Z"
   end = input("Enter end date (YYYY-MM-DD): ") + "T23:59:59Z"

   df = fetch_data(start, end)
   print(df.head())
    
if __name__ == "__main__":
    main()