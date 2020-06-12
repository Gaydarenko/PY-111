from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    print(g.adj, starting_node)
    hist = {}
    res = {}
    queue = [starting_node, ]
    parent_cost = {starting_node: 0}
    while queue:
        if not hist.get(queue[0], None):
            hist[queue[0]] = 1
            for node in g.nodes:
                res[node] = {queue[0]: }
            parent_cost.pop(queue[0])
            queue.pop(0)

    return None


# if __name__ == '__main__':
#     c = nx.DiGraph
#     a = {'A': {'B': {'weight': 1}}, 'B': {'C': {'weight': 3}, 'E': {'weight': 8}, 'D': {'weight': 2}}, 'C': {'E': {'weight': 4}, 'D': {'weight': 1}}, 'D': {'E': {'weight': 2}, 'A': {'weight': 2}}, 'E': {'F': {'weight': 3}}, 'F': {}, 'G': {'D': {'weight': 1}}}
#     b = 'A'
#     n = a.keys()
#     c.add_nodes_from(n)
#     print(n)
#     for x in a:
#         c.add_node(x)
#         print(f'node1 - {x}, node2 {a[x]}')
#         # c.add_edge(x, a[x])
#     print(dijkstra_algo(c, b))
