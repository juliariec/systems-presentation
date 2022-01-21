import json
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from plotly_example_graph import fig

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

fig.update_layout(clickmode='event+select')

fig.update_traces(marker_size=20)

app.layout = html.Div([
    html.H1(children='Graph Visualization', style={'textAlign': 'center'}),

    dcc.Graph(
        id='network-graph',
        figure=fig
    ),

    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown("""
                **Click Data**

                Click on points in the graph.
            """),
            html.Pre(id='click-data', style=styles['pre']),
        ], className='three columns'),
    ])
])


@app.callback(
    Output('click-data', 'children'),
    Input('network-graph', 'clickData'))
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)


if __name__ == '__main__':
    app.run_server(debug=True)
