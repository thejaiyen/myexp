import networkx as nx
import matplotlib.pyplot as plt
# Ghaph 1 as G
G = nx.Graph()
print(G)

# ---------------------------------------------------------------------------
# /// add node
print("-"*10,"Node","-"*10) 
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
print("add node from adding edge (1, 6) is " ,list(G))

# /// remove node
# remove single 
G.remove_node(6)
print("remove single node (6) is " ,list(G))

# remove node from list
G.remove_nodes_from([4, 5])
print("remove from list (4,5) is " ,list(G))

# ---------------------------------------------------------------------------
# /// add edge
print("\n","-"*10,"Edge","-"*10)
# add singe edge
G.add_edge(1, 2)
print("add single edge is " ,list(G.edges) ," ,node is ",list(G))
# add edge from list
G.add_edges_from([(1, 3), (2, 3),(1,4)])
print("add from list is " ,list(G.edges)," ,node is ",list(G))
print("adding edge = adding node")

# ---------------------------------------------------------------------------
# /// print
print("\n","-"*10,"print","-"*10)

# node
print("list(G) is ",list(G))
print("G.nodes is ",G.nodes)

# edgs
print("list(G.edges) is ",list(G.edges))
print("G.edges is ",G.edges)

# adjacency 
print("G.adj is ",G.adj)
print("G.adj[1] is ",G.adj[1])

# ---------------------------------------------------------------------------
# /// add edge
nx.draw(G,with_labels=True)
plt.show