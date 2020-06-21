import networkx as nx
import matplotlib.pyplot as plt


def print_graph(graph):
    pos = nx.spring_layout(graph)
    labels = {node: str(node) for node in graph.nodes()}

    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos, labels, font_size=12)

    plt.show()


# Можно было бы импортировать из е0_breath_first_search, но он пока в другой ветке
def my_bfs(g, start_node):
    viewed = [start_node, ]
    queue = [start_node, ]

    while len(queue):
        n = queue.pop(0)
        for neighbor in g.neighbors(n):
            if neighbor not in viewed:
                queue.append(neighbor)
                viewed.append(neighbor)

    return viewed


def check_tree(gr):
    # проверка на то что это неориентированный граф и соотношение кол-ва вершин и ребер
    if type(gr) != nx.classes.graph.Graph or len(gr.nodes) - 1 != len(gr.edges):
        return False

    # проверка на наличие петель
    for node in gr.nodes():
        if node in gr.neighbors(node):
            return False

    # проверка связности поиском в ширину
    if set(gr.nodes) != set(my_bfs(gr, tuple(gr.nodes)[0])):
        return False

    return True


if __name__ == '__main__':
    # graph = nx.DiGraph()
    # graph.add_nodes_from("ABCDEFG")
    # graph.add_weighted_edges_from([
    #     ('A', 'B', 1),
    #     ('B', 'C', 3),
    #     ('C', 'E', 4),
    #     ('E', 'F', 3),
    #     ('B', 'E', 8),
    #     ('C', 'D', 1),
    #     ('D', 'E', 2),
    #     ('B', 'D', 2),
    #     ('G', 'D', 1),
    #     ('D', 'A', 2)
    # ])
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        # ('A', 'A'),
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('C', 'G'),
        ('D', 'H'),
        ('E', 'I'),
        ('E', 'J')
    ])

    print(check_tree(graph))
    # print_graph(graph)
