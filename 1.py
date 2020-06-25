# l = [str(i)+str(i-1) for i in range(20)]
# print(l)
# with open('3.txt', 'w') as file:
#     for i in l:
#         file.write(str(i) + '\n')
# f = open('3.txt', 'w')
# for i in l:
#     f.write(i + '\n')
# f.close()

# import collections
# a = collections.defaultdict(lambda: 42)
# # a['x'] = 10
# print(a)
# print(a['x'])
#
#

import numpy as np
import json
import tkinter as tk
import tkinter.messagebox as mb


a = [["Унесенные ветром", "Евген у.К.", "наука"],
     ["Физика", "Евген", "наука"],
     ["Алгебра", "Евген", "наука"],
     ["Химия", "Евген", "наука"],
     ["Ботаника", "Елена", "наука"],
     ["Физ-ра", "Евген", "спорт"]]

# with open('2.txt', 'w', encoding='utf-8') as file:
#      json.dump(a, file, ensure_ascii=False)

# with open('search.txt', 'r', encoding='utf-8') as file:
#      a = json.load(file.readlines())
#      print(a)

# title = 'Физика'
# author = 'Евген'
# genre = 'наука'
#
# for i in a:
#      with open('search.txt', 'a', encoding="utf-8") as file:
#           json.dump(i, file, ensure_ascii=False)


with open('catalog.lib', 'r', encoding="utf-8") as file:
     # print(len(file.readline()))
     # print(file.readline())
     f = file.readlines()
     f.sort()
for i in f:
     print(json.loads(i))

# with open('search.txt', 'a', encoding="utf-8") as file:
#      file.seek(-2, 2)
#      file.writelines("-1")


#
# print(type(a))
# print(a)
# # print(a[:, 1])
# a = np.array(a)
# print(type(a))
# print(a)
# b = a[:, 1]
# print(b)
# c = np.where(b == 'Евген')
# print(set(c[0]))
# print(type(c[0]))
