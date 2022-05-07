import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])

# Clean data
df=df.loc[
  (df['value'] >= df['value'].quantile(0.025)) &
  (df['value'] <= df['value'].quantile(0.975)) ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 5))
    ax = sns.lineplot(data=df, x="date", y="value",color='r')
    ax.set(xlabel="Date",ylabel="Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
 
    #df_bar = df.groupby([df.date.dt.year,df.date.dt.month])['value'].mean()
    df_bar=df.copy()
    df_bar['Years']=df.date.dt.year
    df_bar['Months']=df.date.dt.month
    df_bar.pop('date')
    df_bar=pd.melt(df_bar, id_vars=['Years','Months'], value_vars=['value'])
    df_bar=df_bar.groupby(['Years','Months'], as_index=False)['value'].mean()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(16, 10))
    ax = sns.barplot(data=df_bar,x='Years',y='value',hue='Months')
    labels=[
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"]
    ax.set(xlabel="Years",ylabel="Average Page Views")
    h, l = ax.get_legend_handles_labels()
    ax.legend(h, labels, title="Months")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    print(df_box.head())
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

    ax1=sns.boxplot( x=df_box['year'], y=df_box['value'], data=df_box,ax=ax1)
    ax1.set(xlabel="Year",ylabel="Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")
    order=[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
    ax2=sns.boxplot( x=df_box['month'], y=df_box['value'], data=df_box,ax=ax2,order=order)
    ax2.set(xlabel="Month",ylabel="Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
