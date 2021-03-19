import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('Pattern_Recognised.csv')

fig = go.Figure(data=[go.Candlestick(x=df[df.columns[0]],
                open=df[df.columns[1]], high=df[df.columns[2]],
                low=df[df.columns[3]], close=df[df.columns[4]])
                     ])

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()
