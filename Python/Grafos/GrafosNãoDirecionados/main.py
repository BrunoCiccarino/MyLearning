import networkx as nx
import matplotlib.pyplot as plt


"""Aqui vou criar uma função que cria um grafo não direcionado, vou adicionar os vértices (ou nós) e vou adicionar as arestas (conexões entre os vertices)"""

def grafoN():
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 1)])
    return G

G = grafoN()

print("Número de nós:", G.number_of_nodes())
print("Número de arestas:", G.number_of_edges())
print("Nós:", list(G.nodes()))
print("Arestas:", list(G.edges()))

