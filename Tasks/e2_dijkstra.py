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
    costs = nx.get_edge_attributes(g, 'weight')
    for x in g.nodes:
        res[x] = ('', float('inf'))
    res[starting_node] = ('', 0)
    queue = [(starting_node, 0), ]
    while queue:
        target = queue.pop(0)
        if hist.get(target[0]):
            continue
        else:
            hist[target[0]] = ''
        for node in g.neighbors(target[0]):
            parent_cost = (target[0], costs[(target[0], node)])
            if parent_cost[1] + target[1] < res[node][1]:
                res[node] = (parent_cost[0], parent_cost[1] + target[1])
                queue.append((node, parent_cost[1] + target[1]))
    for x in res:
        res[x] = res[x][1]
    return res
