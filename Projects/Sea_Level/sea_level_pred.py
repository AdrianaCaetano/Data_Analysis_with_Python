import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('/content/epa-sea-level.csv')

    # Create scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis
    plt.subplots(figsize=(15, 5))
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y, label='original data')

    # Create first line of best fit
    reg = linregress(x , y)

    # Make the line go through the year 2050 to predict the sea level rise in 2050
    end_year = df['Year'].max()
    df = df.append([{'Year': year} for year in range(end_year + 1, 2050)])
    x = df['Year'] # update x 

    # Add first line of best fit to plot
    plt.plot(x, reg.intercept + reg.slope*x, color='r', label='first best fit')

    # Filter data from year 2000 through the most recent year in the dataset
    df_recent = df[(df['Year'] >= 2000) & (df['Year'] <= end_year)]
    x = df_recent['Year'] # update x values
    y = df_recent['CSIRO Adjusted Sea Level'] # update y values

    # Create second line of best fit using data from year 2000 through the most recent year
    recent_reg = linregress(x , y)

    # Make the line go from 2000 through 2050
    df_recent = df_recent.append([{'Year': year} for year in range(end_year + 1, 2050)])
    x = df_recent['Year'] # update x values
    
    # Add second line of best fit to plot
    plt.plot(x, recent_reg.intercept + recent_reg.slope*x, color='g', linestyle='dashed', label='second best fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    #plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
