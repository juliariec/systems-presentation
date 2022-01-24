import os
import gunicorn
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from graph import fig

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1(
        children='Exploring Social Connectedness', 
        style={'textAlign': 'center'}
    ),

    dcc.Graph(
        id='network-graph',
        figure=fig
    ),

    html.Div(className='row', children=[
        html.Div(id='click-data'),
    ])
])


@app.callback(
    Output('click-data', 'children'),
    Input('network-graph', 'clickData'))
def display_click_data(clickData):
    title = 'No node selected'
    info = 'Please select a node to view related information.'

    if isinstance(clickData, dict):
        title = clickData['points'][0]['text']
        info = clickData['points'][0]['customdata'] 

    return html.Div([
        html.H2(
            children=title,
            style={'textAlign': 'center'}
        ),
        dcc.Markdown(
            children=info, 
            style={'margin': '0 auto', 'padding': '0 1rem', 'maxWidth': '800px'}
        )
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
