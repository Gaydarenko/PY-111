# import networkx as nx
# import matplotlib.pyplot as plt

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
print(G2.edges)  # показывает все ребра
print(list(G2.neighbors('b')))  # показывает соседей
print(G2['b'])  # показывает вершины и ребра к ним, а также вес
print(G2.adj['b'])  # аналогично
print(G2['b']['d'])  # показывает вес ребра
for i in G2.nodes:
    print(i)
# nx.draw(G2, with_labels=True)
# plt.show()
print(G2.adj)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# test = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]
# test = [0] + test
# d0 = nx.DiGraph()
# for i in range(len(test)):
#      d0.add_node(f't{i}')
# test_edges = []
# for i in range(len(test)-1):
#     d0.add_edge(f't{i}', f't{i + 1}', weight=(test[i+1] - test[i]))
# for i in range(len(test)-2):
#     d0.add_edge(f't{i}', f't{i + 2}', weight=(test[i+2] - test[i]))
# print(d0.nodes)
# print(d0.edges)
#
# # nx.draw(d0, with_labels=True)
# # plt.show()
# q = list(d0.nodes)
# viewed = []
# queue = []
# n = q.pop(0)
# viewed.append(n)
# queue.append(n)
# while True:
#     n = queue.pop(0)
#     for node in d0.neighbors(n):
#         if node not in viewed:
#             viewed.append(node)
#             queue.append(node)

# import numpy as np
# def calculate_paths(shape: (int, int), point: (int, int)) -> int:
#     """
#     Given field with size rows*cols count available paths from (0, 0) to point
#     :param shape: tuple of rows and cols (each from 1 to rows/cols)
#     :param point: desired point for horse
#     :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
#     """
#     counter = np.zeros((shape[0], shape[1]), dtype=int)
#     counter[1, 2] = 2
#     counter[2, 1] = 2
#     for i in range(1, counter.shape[1]):
#         for j in range(counter.shape[0]):
#             if counter[j, i] != 0:
#                 if i+1 <= shape[1]-1 and j+2 <= shape[0]-1:
#                     counter[j+2, i+1] += counter[j, i] * 2
#                 if i+2 <= shape[1]-1 and j+1 <= shape[0]-1:
#                     counter[j+1, i+2] += counter[j, i] * 2
#                 if j - 1 >= 0 and i + 2 <= shape[1]-1:
#                     counter[j-1, i+2] += counter[j, i] * 2
#                 if j-2 >= 0 and i+1 <= shape[1]-1:
#                     counter[j-2, i+1] += counter[j, i] * 2
#     print(counter)
#     return counter[point[0], point[1]]

# import tkinter as tk
# # from tkinter import *
#
# root = tk.Tk()
#
# e = tk.Entry(width=20)
# b = tk.Button(text="Преобразовать")
# l = tk.Label(bg='black', fg='white', width=20)
#
#
# def strToSortlist(event):
#     s = e.get()
#     s = s.split()
#     s.sort()
#     l['text'] = ' '.join(s)
#
#
# b.bind('<Button-1>', strToSortlist)
#
# e.pack()
# b.pack()
# l.pack()
# root.mainloop()

# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# fib = [-1 for _ in range(100)]
#
# def get_fib(i):
#     if (i <= 2):
#         return 1
#     if (fib[i] != -1):
#         return fib[i]
#     fib[i] = get_fib(i - 1) + get_fib(i - 2)
#     return fib[i]
#
# print(get_fib(6))
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

# def ball(floor):
#     if floor < 1:
#         return 0
#     if floor == 1:
#         return 1
#     if floor == 2:
#         return 2
#     if floor == 3:
#         return 4
#     return ball(floor - 1) + ball(floor - 2) + ball(floor - 3)
#
# print(ball(4))

# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
def pay_stairway(costs, floor):
    """
    Для расчета самого дешевого пути до указанной ступеньки
    :param costs:
    :param floor:
    :return:
    """
    if floor < 0:
        return 0
    return costs[floor - 1] + min(pay_stairway(costs, floor - 1), pay_stairway(costs, floor - 2))


print(pay_stairway([3, -2, 4, 5, 0], 5))


def pay_stair_end(costs):
    if len(costs) == 0:
        return 0
    return costs[-1] + min(pay_stair_end(costs[:-1]), pay_stair_end(costs[:-2]))


print(pay_stair_end([3, -2, 4, 5, 0]))

