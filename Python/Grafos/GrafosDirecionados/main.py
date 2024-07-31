import networkx as nx
import matplotlib.pyplot as plt

def criar_grafo_direcionado():
    G = nx.DiGraph()
    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 1)])
    return G

grafo_dir = criar_grafo_direcionado()

print("Número de nós:", grafo_dir.number_of_nodes())
print("Número de arestas:", grafo_dir.number_of_edges())
print("Nós:", list(grafo_dir.nodes()))
print("Arestas:", list(grafo_dir.edges()))

