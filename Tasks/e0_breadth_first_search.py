from typing import Hashable, List
import networkx as nx
import matplotlib.pyplot as plt


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    print(g.nodes, start_node)
    viewed = [start_node, ]
    queue = [start_node, ]
    while len(queue):
        n = queue.pop(0)
        for neighbor in g.neighbors(n):
            if neighbor not in viewed:
                queue.append(neighbor)
                viewed.append(neighbor)

    return viewed


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'D'),
        ('H', 'E'),
        ('H', 'J'),
        ('E', 'D'),
    ])
    # nx.draw(graph, with_labels=True)
    # plt.show()
    print('!')
    bfs(graph, 'A')