import networkx as nx
import matplotlib.pyplot as plt

# G1 = nx.Graph()
G2 = nx.DiGraph()
# G3 = nx.MultiDiGraph()

a = list('abcdefgh')
# print(a)
G2.add_nodes_from(a)
b = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('a', 'f'),
     ('b', 'c'), ('b', 'e'),
     ('c', 'd'),
     ('d', 'e'),
     ('e', 'f'),
     ('f', 'c'), ('f', 'g'), ('f', 'h'),
     ('g', 'f'), ('g', 'h'),
     ('h', 'g'), ('h', 'f')]
G2.add_edge('b', 'd', weight=2)
G2.add_edges_from(b)
print(G2.nodes)
print(G2.edges)         # показывает все ребра
print(list(G2.neighbors('b')))      # показывает соседей
print(G2['b'])          # показывает вершины и ребра к ним, а также вес
print(G2.adj['b'])      # аналогично
print(G2['b']['d'])     # показывает вес ребра

nx.draw(G2, with_labels=True)
plt.show()
