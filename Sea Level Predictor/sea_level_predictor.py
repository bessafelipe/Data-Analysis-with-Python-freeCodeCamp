import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  plt.figure(1, figsize=(16, 9))
  df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
  res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  plt.plot(np.arange(1880,2051), res.intercept + (res.slope * np.arange(1880,2051)), 'r')
    # Create second line of best fit
  res2 = linregress(df.loc[df.Year>=2000]['Year'], df.loc[df.Year>=2000]['CSIRO Adjusted Sea Level'])
  plt.plot(np.arange(2000,2051), res2.intercept + res2.slope*np.arange(2000,2051), 'g')
    # Add labels and title
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()