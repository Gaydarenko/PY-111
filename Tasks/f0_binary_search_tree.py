"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
import networkx as nx
import json

NODE = {
    'key': None,
    'value': None,
    'left': None,
    'right': None
}

tree = {}


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    # global tree
    print(key, value)
    # graph = nx.Graph()
    # if not graph.nodes:
    #     graph.add_node(key)
    # global tree

    # if not tree:
    #     tree['key'] = key
    #     tree['value'] = value
    #     # tree['left'] = None
    #     # tree['right'] = None
    # else:
    #     if key > tree[key]:
    #         if
    #         tree['right'] = insert(key, value)
    #     elif key < tree[key]:
    #         tree['left'] = insert(key, value)
    # # print(tree)
    # return tree
    global tree

    def _ins(node):
        if  node['key'] < key:
            if node['right'] is None:
                node['right'] = NODE.copy()
                node['right'].update(key=key, value=value)
            else:
                _ins(node['right'])
        else:
            if node['left'] is None:
                node['left'] = NODE.copy()
                node['left'].update(key=key, value=value)
            else:
                _ins(node['left'])
    if not tree:
        tree = NODE.copy()
        tree.update(key=key, value=value)
    else:
        _ins(tree)


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    print(key)
    return None


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    print(key)
    return None


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    return None


if __name__ == '__main__':
    tree = {}
    insert(42, 'The meaning of life, the universe and everything.')
    insert(0, 'ZERO!')
    insert(13, "Devil's sign here")
    insert(13, "Oh no, devil's sign again Oo")
    print(json.dumps(tree, indent='\t'))

