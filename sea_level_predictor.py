import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Line of best fit (full dataset)
    regress_full = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_full = pd.Series(range(1880, 2051))
    y_full = regress_full.slope * x_full + regress_full.intercept
    plt.plot(x_full, y_full, color="red")

    # Line of best fit (year 2000+)
    df_recent = df[df["Year"] >= 2000]
    regress_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = regress_recent.slope * x_recent + regress_recent.intercept
    plt.plot(x_recent, y_recent, color="green")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save image and return figure
    plt.savefig("sea_level_plot.png")
    fig = plt.gcf()
    return fig
