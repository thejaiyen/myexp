import matplotlib.pyplot as plt
import networkx as nx



dirr = "./input02.csv"
edges = []
edge_labels = {}
workbook = open(dirr)
data = workbook.readlines()
for i in data:
    i = i.split(",")
    edges.append ([i[0],i[2]])
    edge_labels.update({(i[2],i[0]): i[1]})

# print(edges)
# print(edge_labels)



G = nx.Graph()
G.add_edges_from(edges)
print('G is ',G)
# pos = nx.spring_layout(G,k=5,scale=5)
pos = nx.kamada_kawai_layout(G, scale=1000)
print("pos................", pos)
print("\n")
plt.figure()
nx.draw(
    G, pos,  node_color='pink',node_size=1000,
    labels={node: node for node in G.nodes()}
)

nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=edge_labels,
    font_color='red',
    label_pos=0.3
)
# plt.axis('off')
# plt.show()
plt.savefig("hi.jpg")

print(G.adj)