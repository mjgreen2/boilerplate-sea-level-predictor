#####################################################################
#Solution to Sea Level Predictor project
#Created in Visual Studio Code
#by Michael Green
#####################################################################

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file. Use Pandas to import the data from epa-sea-level.csv.
    df = pd.DataFrame(pd.read_csv(filepath_or_buffer = "epa-sea-level.csv"))

    # Create first line of best fit. Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
    overall_time = np.arange(1880, 2051, 1)

    first_line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    overall_trend = pd.Series([first_line.intercept + first_line.slope*i 
                                for i in overall_time]
                            )
    overall_trend.name = "Overall Trend"

    # Create second line of best fit. Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    modern_time = np.arange(2000, 2051, 1)
    df_modern = df[df['Year']>= 2000]

    second_line = linregress(df_modern['Year'], 
                            df_modern['CSIRO Adjusted Sea Level']
                            )
    modern_trend = pd.Series([second_line.intercept + second_line.slope*i 
                                for i in modern_time]
                            )
    modern_trend.name = "Modern Trend"

    # Create scatter plot. Use matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axis.
    # Add labels and title. The x label should be "Year", the y label should be "Sea Level (inches)", and the title should be "Rise in Sea Level".
    fig, ax = plt.subplots(figsize = (12, 8))
    ax.title.set_text("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_xlim(1880, 2075)
    ax.set_xticks(np.arange(1850.0, 2100.0, step=25))
    ax.set_ylim(-2, 16)

    plt.scatter(x = df['Year'], 
                y = df['CSIRO Adjusted Sea Level'], 
                marker = 'o', 
                label='Original Data'
                )
    plt.plot(overall_time, overall_trend, 'r', label='Overall Line')
    plt.plot(modern_time, modern_trend, 'g', label='Modern Line')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()