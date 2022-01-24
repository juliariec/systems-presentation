import plotly.graph_objects as go
import networkx as nx
import pandas as pd

nodes_df = pd.read_csv('nodes.csv')
edges_df = pd.read_csv('edges.csv')

G = nx.from_pandas_edgelist(edges_df, 'source', 'target')

for i in sorted(G.nodes()):
    G.nodes[i]['x'] = nodes_df.x[i]
    G.nodes[i]['y'] = nodes_df.y[i]
    G.nodes[i]['label'] = nodes_df.label[i]
    G.nodes[i]['data'] = nodes_df.data[i]

edge_x = []
edge_y = []

for edge in G.edges():
    x0 = G.nodes[edge[0]]['x']
    y0 = G.nodes[edge[0]]['y']
    x1 = G.nodes[edge[1]]['x']
    y1 = G.nodes[edge[1]]['y']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
node_labels = []
node_info = []
for node in G.nodes():
    x = G.nodes[node]['x']
    y = G.nodes[node]['y']
    node_x.append(x)
    node_y.append(y)
    node_labels.append(G.nodes[node]['label'])
    node_info.append(G.nodes[node]['data'])

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='Blues',
        reversescale=False,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

node_adjacencies = []
for node, adjacencies in enumerate(G.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))

node_trace.text = node_labels
node_trace.marker.color = node_adjacencies
node_trace.customdata = node_info

fig = go.Figure(
    data=[edge_trace, node_trace],
    layout=go.Layout(
        showlegend=False,
        hovermode='closest',
        margin=dict(b=40,l=5,r=5,t=40),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )
)

fig.update_layout(clickmode='event+select')
fig.update_traces(marker_size=15)