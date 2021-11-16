import matplotlib.pyplot as plt
import networkx as nx

# draw_networkx_edge_labels

edges = [['A', 'B'], ['B', 'C'], ['B', 'D']]
G = nx.Graph()
G.add_edges_from(edges)
pos = nx.spring_layout(G)
print( pos)
plt.figure()
nx.draw(
    G, pos, edge_color='black', width=1, linewidths=1,
    node_size=1000, node_color='pink', alpha=0.9,
    labels={node: node for node in G.nodes()}
)

nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={('A', 'B'): 'AB', ('B', 'A'): 'BA',
                 ('B', 'C'): 'BC', 
                 ('B', 'D'): 'BD'},
    font_color='red',
    label_pos=0.15
)
# plt.axis('off')
plt.show()

print(G.adj)