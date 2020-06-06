import networkx as nx
import matplotlib.pyplot as plt

# G1 = nx.Graph()
# G2 = nx.DiGraph()
# # G3 = nx.MultiDiGraph()
#
# a = list('abcdefgh')
# # print(a)
# G2.add_nodes_from(a)
# b = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('a', 'f'),
#      ('b', 'c'), ('b', 'e'),
#      ('c', 'd'),
#      ('d', 'e'),
#      ('e', 'f'),
#      ('f', 'c'), ('f', 'g'), ('f', 'h'),
#      ('g', 'f'), ('g', 'h'),
#      ('h', 'g'), ('h', 'f')]
# G2.add_edge('b', 'd', weight=2)
# G2.add_edges_from(b)
# print(G2.nodes)
# print(G2.edges)  # показывает все ребра
# print(list(G2.neighbors('b')))  # показывает соседей
# print(G2['b'])  # показывает вершины и ребра к ним, а также вес
# print(G2.adj['b'])  # аналогично
# print(G2['b']['d'])  # показывает вес ребра

# nx.draw(G2, with_labels=True)
# plt.show()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

test = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]
test = [0] + test
d0 = nx.DiGraph()
for i in range(len(test)):
     d0.add_node(f't{i}')
test_edges = []
for i in range(len(test)-1):
    d0.add_edge(f't{i}', f't{i + 1}', weight=(test[i+1] - test[i]))
for i in range(len(test)-2):
    d0.add_edge(f't{i}', f't{i + 2}', weight=(test[i+2] - test[i]))
print(d0.nodes)
print(d0.edges)

# nx.draw(d0, with_labels=True)
# plt.show()
q = list(d0.nodes)
viewed = []
queue = []
n = q.pop(0)
viewed.append(n)
queue.append(n)
while True:
    n = queue.pop(0)
    for node in d0.neighbors(n):
        if node not in viewed:
            viewed.append(node)
            queue.append(node)