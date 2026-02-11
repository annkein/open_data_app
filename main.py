from api_client import fetch_data
from visualization import plot_data

def main():
    start = input("Enter start date (YYYY-MM-DD): ") + "T00:00:00Z"
    end = input("Enter end date (YYYY-MM-DD): ") + "T23:59:59Z"

    try:
        df = fetch_data(start, end)
        print("\nData preview (first 10 rows):")
        print(df.head(10).to_string(index=False))

        print(f"\nTotal rows returned: {len(df)}")
        print(
            f"Time range in data: "
            f"{df['startTime'].min()} -> {df['startTime'].max()}"
        )

        print("\nSummary statistics:")
        print(f"Average consumption: {df['Electricity consumption (MW)'].mean():.1f} MW")
        print(f"Minimum consumption: {df['Electricity consumption (MW)'].min():.1f} MW")
        print(f"Maximum consumption: {df['Electricity consumption (MW)'].max():.1f} MW")

        plot_data(df)

    except Exception as e:
        print(f"Error: {e}")
    

if __name__ == "__main__":
    main()