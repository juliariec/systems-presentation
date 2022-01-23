import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from plotly_test_graph import fig

##external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
##app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        children='Graph Visualization', 
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
        html.P(
            children=info,
            style={'textAlign': 'center'}
        ),
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
