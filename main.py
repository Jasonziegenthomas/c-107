import pandas as pd
import csv
import plotly.express as px

df=pd.read_csv('data.csv')
student_df=df.loc[df['student_id']=='TRL_987']

fig=px.Figure(px.scatter(
    x=student_df.groupby('level')['attempt'].mean(),
    y=['Level 1','Level 2','Level 3','Level 4'],
    orientation='h'))
fig.show()