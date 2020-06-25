from typing import Hashable, List
import networkx as nx
import matplotlib.pyplot as plt


def dfs(g: nx.Graph, start_node: Hashable, viewed=None) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    print(g, start_node)
    # queue = [start_node, ]
    # viewed = [start_node, ]
    # res = []
    # while len(queue):
    #     n = queue.pop()
    #     res.append(n)
    #     for neighbor in g.neighbors(n):
    #         if neighbor not in viewed:
    #             queue.append(neighbor)
    #             viewed.append(neighbor)
    # return res

    # viewed = {}
    # def my_dfs(gr, node):
    #     viewed[node] = 0
    #     for neighbor in gr.neighbors(node):
    #         if viewed.get(neighbor) is None:
    #             my_dfs(gr, neighbor)
    # my_dfs(g, start_node)
    # return list(viewed.keys())

    if viewed is None:
        viewed = {}
    viewed[start_node] = 0
    for neighbor in g.neighbors(start_node):
        if viewed.get(neighbor) is None:
            dfs(g, neighbor, viewed)
    return list(viewed.keys())


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'G'),
    ])
    # nx.draw(graph, with_labels=True)
    # plt.show()
    print('!')
    print(dfs(graph, 'A'))
