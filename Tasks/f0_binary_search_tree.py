"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
import networkx as nx
import json

tree = {}


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global tree
    print(key, value)
    # graph = nx.Graph()
    # if not graph.nodes:
    #     graph.add_node(key)

    def my_insert(my_tree):
        if not my_tree:
            return my_tree.update({'key': key, 'value': value})
        elif key > my_tree['key']:
            if my_tree.get('right') is None:
                return my_tree.update({'right': {'key': key, 'value': value}})
            else:
                return my_insert(my_tree['right'])
        elif key < my_tree['key']:
            if my_tree.get('left') is None:
                return my_tree.update({'left': {'key': key, 'value': value}})
            else:
                return my_insert(my_tree['left'])
    return my_insert(tree)


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
    global tree

    def my_find(massive):
        if massive is None:
            raise KeyError
        if massive['key'] == key:
            return massive['value']
        elif key > massive['key']:
            if massive.get('right') is None:
                raise KeyError
            else:
                return my_find(massive['right'])
        elif key < massive['key']:
            if massive.get('left') is None:
                raise KeyError
            else:
                return my_find(massive['left'])
    return my_find(tree)


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
    print(find(42))
    print(find(13))
    print(find(-999))
