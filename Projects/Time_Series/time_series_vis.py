import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('/content/fcc-forum-pageviews.csv',
                 parse_dates=[0],
                 index_col=[0]
                 )
df.rename(columns={"value": "daily_views"}, inplace=True)

# Clean data
df = df[
        (df["daily_views"] >= df["daily_views"].quantile(0.025)) &
        (df["daily_views"] <= df["daily_views"].quantile(0.975))
    ]

def draw_line_plot():
    ''' A function that uses Matplotlib to draw a line chart to visualize the 
    Daily freeCodeCamp Forum Page Views from 5/2016 to 12/2019. 
    '''
    # Draw line plot
    fig,ax = plt.subplots(figsize=(15, 5))
    fig = plt.plot(df, color='red', linewidth=1)
  
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019') 
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    ''' A function that draws a bar chart that shows the average daily page views
    for each month grouped by year. 
    '''
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(pd.Grouper(freq="M")).mean().rename(columns={'daily_views': 'avg'})

    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month_name()
    
    # Draw bar plot
    fig,ax = plt.subplots(figsize=(10,10))
    ax = sns.barplot(
        data=df_bar,
        x='year', 
        y='avg', 
        hue='month', 
        hue_order = ['January','February','March','April','May','June','July',
                'August','September','October','November','December'],
    )
    ax.set(xlabel = 'Years',ylabel = 'Average Page Views', )
    plt.legend(title='Months', loc='upper left')
    plt.title('Average freeCodeCamp Page Views by Month')
  
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    ''' A function that uses Seaborn to draw two adjacent box plots to show how 
    the values are distributed within a given year or month and how it compares over time. 
    The first chart is a Year-wise Box Plot (Trend) and the second chart is a 
    Month-wise Box Plot (Seasonality). 
    '''
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax1, ax2 = plt.subplots(1,2, figsize=(15,10))

    # Left plot
    sns.boxplot(ax=ax1, 
                data=df_box, 
                x=df_box['year'], 
                y=df_box['daily_views']
                )
    ax1.set(xlabel='Year', 
            ylabel='Page Views', 
            title='Year-wise Box Plot (Trend)'
            )

    # Right plot
    sns.boxplot(ax=ax2,
            data=df_box,
            x=df_box['month'],
            y=df_box['daily_views'],
            order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
            )
    ax2.set(xlabel='Month', 
            ylabel='Page Views', 
            title='Month-wise Box Plot (Seasonality)'
            )

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
