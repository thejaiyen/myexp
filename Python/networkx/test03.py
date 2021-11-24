import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edge(1, 2)
H = nx.DiGraph(G)  # create a DiGraph using the connections from G
print(list(H.edges()))
subax1 = plt.subplot(131)
nx.draw(H,with_labels=True)

edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.Graph(edgelist)  # create a graph from an edge list
print(list(H.edges()))
subax1 = plt.subplot(132)
nx.draw(H,with_labels=True)

adjacency_dict = {0: (1, 2), 1: (0, 2), 2: (0, 1)}
H = nx.Graph(adjacency_dict)  # create a Graph dict mapping nodes to nbrs
print(list(H.edges()))
subax1 = plt.subplot(133)
nx.draw(H,with_labels=True)

plt.show()