import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file

    data = 'epa-sea-level.csv'
    df = pd.read_csv(data)

    # Create scatter plot

    x = df.Year
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y, color = 'black', s=1)

    # Create first line of best fit

    new_x = np.arange(1880,2051,1)
    res = linregress(x,y)
    plt.plot(new_x, res.intercept + res.slope*new_x,
            'r',
            label='fitted line',
            linewidth = 1
            )

    # Create second line of best fit

    new_data = df[df['Year'] >= 2000]
    x2 = new_data.Year
    y2 = new_data['CSIRO Adjusted Sea Level']
    new_x2 = np.arange(2000,2051,1)
    res2= linregress(x2,y2)
    plt.plot(new_x2, res2.intercept + res2.slope*new_x2,
            'b',
            label='fitted line',
            linewidth = 1)

    # Add labels and title

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()