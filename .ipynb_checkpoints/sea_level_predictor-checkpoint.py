import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df.Year, df["CSIRO Adjusted Sea Level"] , label='original data')


    # Create first line of best fit
    res = linregress(df.Year, df["CSIRO Adjusted Sea Level"])
    ax.plot(df.Year, res.intercept + res.slope*df.Year, 'r', label='fitted line')

    years_extended = np.arange(df['Year'].min(), 2051)
    line_extended = res.slope * years_extended + res.intercept

    ax.plot(years_extended, line_extended, 'r', label='Line of Best Fit')


    # Create second line of best fit
    df_reduced = df[df.Year >= 2000]
    res = linregress(df_reduced.Year, df_reduced["CSIRO Adjusted Sea Level"])
    ax.plot(df_reduced.Year, res.intercept + res.slope*df_reduced.Year, 'r', label='fitted line')
    
    years_extended = np.arange(df_reduced['Year'].min(), 2051)
    line_extended = res.slope * years_extended + res.intercept
    ax.plot(years_extended, line_extended, 'r', label='Second Line of Best Fit')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot.png')
    return fig.gca()