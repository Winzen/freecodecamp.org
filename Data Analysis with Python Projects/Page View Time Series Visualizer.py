import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#LINK DO TESTE:
#https://replit.com/@LuizSinx/boilerplate-page-view-time-series-visualizer-1#main.py


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=["date"], index_col=[0])

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots()

    df.plot(y='value', color='red', figsize=(15, 5), ax=ax, linewidth=1, legend=False)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    #fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df.index.month
    df_bar = (df_bar.groupby(['year', 'month'])
              ['value'].mean()).unstack()

    # Draw bar plot
    fig, ax = plt.subplots()

    df_bar.plot(kind='bar', legend=True, figsize=(10, 5), ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months',
              labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December'])


    # Save image and return fig (don't change this part)
    #fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    plot_objects = plt.subplots(nrows=1, ncols=2, figsize=(16, 10))
    fig, ((ax, ax2)) = plot_objects

    ax2 = sns.boxplot(data=df_box, x='month', y='value', ax=ax2,
                      order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax = sns.boxplot(data=df_box, x='year', y='value', ax=ax)

    ax.set_title('Year-wise Box Plot (Trend)')
    ax.set_xlabel("Year")
    ax.set_ylabel('Page Views')

    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    #fig.savefig('box_plot.png')
    return fig

if __name__ == '__main__':
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
    plt.show()
