import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "Store": ["Loblaws", "Loblaws", "Loblaws", "No Frills", "No Frills", "No Frills"]
})

fig = px.bar(df, x="Store", y="Amount", color="Fruit", barmode="group")

app.layout = html.Div(children=[
    html.H1(
        children='Fruit Supply', 
        style={'textAlign': 'center'}
    ),

    html.Div(
        children='Be an informed grocery shopper.', 
        style={'textAlign': 'center'}
    ),

    dcc.Graph(
        id='fruit-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)