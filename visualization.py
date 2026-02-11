import matplotlib.pyplot as plt
import pandas as pd

def plot_data(df: pd.DataFrame):
    plt.figure()
    plt.plot(df["startTime"], df["Electricity consumption (MW)"])
    plt.xlabel("Time")
    plt.ylabel("Electricity consumption (MW)")
    plt.title("Electricity consumption in Finland (Fingrid Open Data)")
    plt.tight_layout()
    plt.show()