import networkx as nx
from pyvis.network import Network

color1 =  "purple"
color2 = "green"

g = nx.Graph()

g.add_node(1, label = "JC", title = "Software Developer", color = color1) 
g.add_node(2, label = "AR", title = "Mechanical Engineer", color = color2)
g.add_node(3, label = "RG", title = "Masters Student", color = color1)
g.add_node(4, label = "TC", title = "Accountant", color = color2)
g.add_node(5, label = "EC", title = "Data Scientist", color = color2)
g.add_node(6, label = "AL", title = "Elementary Teacher", color = color1)

g.add_edges_from([(1, 3), (1, 2), (2, 3), (1, 4), (2, 5), (1, 6), (3, 6)])

net = Network()
net.from_nx(g)
net.show("pyvis_test.html")