import networkx as nx
import matplotlib.pyplot as plt
# Ghaph 1 as G
G = nx.Graph()
print(G)
# /// add node
# add single 
G.add_node(1)
print("add single node is " ,list(G))

# add node from list
G.add_nodes_from([2, 3])
print("add node from list is " ,list(G))

# add node with attributes use 2-tuples of the form (node, node_attribute_dict)
G.add_nodes_from([(4, {"color": "red"}),(5, {"color": "green"})])
print("add node with attributes is " ,list(G))

#add node with edge
G.add_edge(1, 6)
print("add node from adding edge is " ,list(G))

# /// remove node
# remove single 
G.remove_node(6)
print("remove single node (6) is " ,list(G))

# remove node from list
G.remove_nodes_from([4, 5])
print("remove from list (4,5) is " ,list(G))


# /// add edge
# add singe edge
G.add_edge(1, 2)
print("add single edge is " ,list(G.edges))

# add edge from list
G.add_edges_from([(1, 3), (2, 3),(1,4)])
print("add from list is " ,list(G.edges))

nx.draw(G,with_labels=True)
plt.show

print(G.adj)