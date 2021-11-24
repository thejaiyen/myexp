import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_edges_from([(1,2),(1,3), (2, 3),(2,4),(5,4),(5,3),(2,7),(4,6)])
print ("Nodes is ",G.nodes,"\nEges is ",G.edges)

print("Short path (1, 6) is ",nx.shortest_path(G, 1, 6))
print("Short path (2, 4) is ",nx.shortest_path(G, 2, 4))

# plot graph
nx.draw(G, with_labels=True)
plt.show()