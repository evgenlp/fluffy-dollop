# задача 1
# import os
# os.chdir('c:/Users/dom2/Desktop')
# print(os.getcwd())
# os.mkdir('экзамен_2')
# os.chdir('экзамен_2')
# print(os.getcwd())
# a = open('test_1.txt', 'w')
# b = open('test_2.txt', 'w')
# c = open('test_3.txt', 'w')
# a.close()
# b.close()
# c.close()
# os.rename('test_1.txt', 'rename_1.txt')
# os.rename('test_2.txt', 'rename_2.txt')
# os.rename('test_3.txt', 'rename_3.txt')
# os.remove('rename_1.txt')
# os.remove('rename_2.txt')
# os.remove('rename_3.txt')
# os.chdir('..')
# os.rmdir('экзамен_2')

# задача 2
# a = [1, 5, 8, 14, 25, 19, 7]
# b = len(a)
# c = 0
# e = []
# for i in a:
#     c += i
# print(b)
# print(c)
# for d in a:
#     if d > c / b:
#         e.append(d)
# print(e)

# задача 3
# a = {1, 2, 3, 5}
# b = {7, 8, 4, 6}
# if a == b:
#     print('множества равны')
# elif len(a) == len(a & b):
#     print('множество 1 \n состоит из множества 2')
# elif len(b) == len(b & a):
#     print('множество 2 \n состоит из множества 1')
# elif len(a & b) > 0:
#     print(a & b)
# else:
#     print('пересечений нет')

# задача 4
# a = 'An apple a day keeps the doctor away'
# c = {}
# for i in a:
#     b = a.count(i)
#     c[i] = b
# print(c)

# задача 5
# a = 0
# b = set([])
# while a < 10:
#     c = int(input("Введите чисо: "))
#     a += 1
#     b.add(c)
# print(b)

# задача 6
# a = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68}
# b = a.values()
# c = a.keys()
# d = 0
# e = []
# f = {}
# for i in b:
#     d += i
# for p in a:
#     if a.get(p) > 5:
#         e.append(p)
#     g = p.split(' ')
#     if len(g) == 1:
#         f[p] = a.get(p)
# print(b)
# print(c)
# print(d, 'общее время звучания всех песен')
# print(e)
# print(f)

# звдвча 7
# a = input('введите строку ')
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(tuple(b))

# задача 8
# a = []
# while True:
#     b = int(input('введите число, 0 завершает ввод: '))
#     if b == 0:
#         break
#     a.append(b)
# a1 = []
# c = int(input('введите нижнее значение диапазона '))
# d = int(input('введитн вержнее значение диапазона '))
# for i in a:
#     if i < c or i > d:
#         a1.append(i)
# for i in range(len(a) - len(a1)):
#     a1.append(0)
# print(a)
# print(a1)

# задача 9
# a = int(input('введите число строк '))
# b = int(input('введите число столбцов '))
# m = []
# for i in range(b):
#     m1 = []
#     for c in range(a):
#         print(i + 1)
#         c1 = int(input('введите число '))
#         m1.append(c1)
#     m.append(m1)
# print(m)
# s = 0
# for i in range(1, a):
#     for c in range(0, i):
#         if m[i][c] < 0:
#             s += 1
# print('колличество отрицательных элементов под главной диагональю матрицы', s)

# задача 10
# a = []
# s = 0
# while True:
#     b = int(input('введите число, 0 прекращает ввод'))
#     if b == 0:
#         break
#     a.append(b)
# c = int(input('введите нижнее значение '))
# d = int(input('введите вержнее значение '))
# for i in a:
#     if i > c and i < d:
#         s += i
# print(s)