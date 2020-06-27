import networkx as nx

# 1)
"""
Оценить асимптотическую сложность приведенного ниже алгоритма:
"""
# a = len(arr) - 1        # O(1) - определение длины массива
# out = list()            # O(1) - созданиие пустого списка (по сути создание одной ссылки на начало)
# while a > 0:            # O(n * (log по основанию 1.7 от n))
#     out.append(arr[a])    # O(n) - вставка в массив - в худшем случае у него с конца не будет места
#                                       и его ВЕСЬ прийдется перезаписывать в другой блок памяти
#     a = a // 1.7          # O(1)
# out.merge_sort()        # O(nlog(n))
# Итоговая сложность = max (т.к. действия последовательны - цикл рассматриваю цельным объектом) - O(nlogn)

# 2)
"""
Дано N человек, считалка из K слогов.
Считалка начинает считать с первого человека.
Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
Игра происходит до тех пор, пока не останется последний человек.
Для данных N и К дать номер последнего оставшегося человека.
"""
def counting(N: int, k: int):
    l = [i for i in range(N)]
    i = k
    while N > 1:
        if N > i:
            l.pop(i)
            N -= 1
            while N > i:
                i += k - 1
                l.pop(i)
                N -= 1
            i -= N
        else:
            i -= N
    return l.pop()

# 3)

def connect_comp(g: nx.Graph):
    """
    Функция происзводит посчет ко   мпонент связности.
    :param g: граф
    :return: коичество компонент связности
    """
    nodes = set(g.nodes())
    n = 0

    while nodes:
        start = nodes.pop()
        queue = [start, ]
        viewed = [start, ]
        res = set()
        while len(queue):
            n = queue.pop()
            res.add(n)
            for neighbor in g.neighbors(n):
                if neighbor not in viewed:
                    queue.append(neighbor)
                    viewed.append(neighbor)

        nodes -= res
        n += 1

    return n

# 7)
"""
Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом
"""
# Если выбирать между теми на которых нам делали акцент (quick/merge), то:
# Целесообразно использовать сортировку слиянием, т.к. много однообразных значений.
# А сортировка слиянием обладает свойством устойчивости.
#
# Но для данного случая я бы выбрал сортировку подсчётом (counting sort)