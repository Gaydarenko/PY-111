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
    # print(key, value)
    # graph = nx.Graph()
    # if not graph.nodes:
    #     graph.add_node(key)

    # Создаю функцию для рекурсивной обработки дерева
    def my_insert(my_tree):
        # Если дерево/поддерево пустое добавляем узел
        if not my_tree:
            return my_tree.update({'key': key, 'value': value})
        # Если ключ больше корневого даноого дерева/поддерева, то...
        elif key > my_tree['key']:
            # Если правый потомок отсутствует, то создать его с ключом и значением
            if my_tree.get('right') is None:
                return my_tree.update({'right': {'key': key, 'value': value}})
            # Если правый потомок уже имеется, перейти в правую ветку и запустить функцию снова
            else:
                return my_insert(my_tree['right'])
        # Если ключ меньше корневого даноого дерева/поддерева, то...
        elif key < my_tree['key']:
            # Если левый потомок отсутствует, то создать его с ключом и значением
            if my_tree.get('left') is None:
                return my_tree.update({'left': {'key': key, 'value': value}})
            # Если левый потомок уже имеется, перейти в правую ветку и запустить функцию снова
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
    global tree

    def my_remove(my_tree):
        if key > my_tree['key']:
            return my_remove(my_tree['right'])
        elif key < my_tree['key']:
            return my_remove(my_tree['left'])
        else:
            my_remove.pair = tuple(my_tree.values())
            if my_tree.get('right') is None and my_tree.get('left') is None:
                return my_tree.clear()
            elif my_tree.get('right') is None:
                return my_tree.update(my_tree.pop('left'))
            elif my_tree.get('left') is None:
                return my_tree.update(my_tree.pop('right'))
            else:
                find_min_in_right(my_tree['right'])
                my_tree.update(find_min_in_right.temp)

    def find_min_in_right(small_tree):
        if small_tree.get('left') is not None:
            if len(small_tree['left'].keys()) > 2:
                return find_min_in_right(small_tree['left'])
            else:
                find_min_in_right.temp = small_tree['left']
                del small_tree['left']
                return small_tree
        elif small_tree.get('right') is not None:
            if len(small_tree['right'].keys()) > 2:
                return find_min_in_right(small_tree['right'])
            else:
                find_min_in_right.temp = small_tree['right']
                del small_tree['right']
                return small_tree
        else:
            find_min_in_right.temp = small_tree.copy()
            return small_tree.clear()
    my_remove(tree)
    return my_remove.pair


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
    insert(53, "Oh no, devil's sign again Oo")
    insert(47, "forty seven")
    insert(80, "eighty")
    print(json.dumps(tree, indent='\t'))
    # print(find(42))
    # print(find(13))
    # print(find(-999))
    print('Function remove start')
    print(remove(42))
    print('Function remove finish')
    print(json.dumps(tree, indent='\t'))
