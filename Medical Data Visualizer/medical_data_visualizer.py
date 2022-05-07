import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight'   df['Event'] = np.where((df.Event == 'Painting'),'Art',df.Event)
BMI=df['weight']/((df['height']/100)**2)
df['overweight'] = np.where((BMI>25),1,0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol']=np.where(df.cholesterol==1,0,1)
df['gluc']=np.where(df.gluc==1,0,1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    value_var=sorted(['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=value_var)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.value_counts().reset_index(name="total")

    # Draw the catplot with 'sns.catplot()'
    fig=sns.catplot(x='variable',y='total', hue='value',col='cardio',data=df_cat, kind='bar', order=value_var)
    fig.set_ylabels("total")
    fig.set_xlabels("variable")
    fig = fig.fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map  
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[
  (df['ap_lo'] <= df['ap_hi']) &
  (df['height'] >= df['height'].quantile(0.025)) &
  (df['height'] <= df['height'].quantile(0.975)) &
  (df['weight'] >= df['weight'].quantile(0.025)) &
  (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax =  plt.subplots(figsize=(12, 9))
    
    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, square=True,annot=True,fmt=".1f",vmin=-0.1,vmax=0.3)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
