# i = 0
# while i < 10:
#     print(i)
#     i = i + 1
# i = 0
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1
# i = 1
# b = 0
# while i <= 50:
#     b += i
#     i += 10
# print(b)
# i = 1
# while i <= 10:
#     print(i ** 2)
#     i += 1
# i = 15
# while i >= 1:
#     print(i)
#     i -= 1
# a = int(input('введте отрицательное число '))
# b = int(input('введите положительное число '))
# while a < b:
#     a = a + 1
#     if a == 0:
#         break
#     print(a)
# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("готово")
# i = 0
# while i < 3:
#     print(i)
#     i += 1
# else:
#     print("Готово")
# i = 7
# a = []
# while i < 100:
#     a.append(i)
#     i += 7
#     len(a)
# print(len(a))
# print(len(a))
# while True:
# a = float(input("введите число с точкой "))
# b = float(input("введите число с точкой "))
# c = input("введите операцию ")
# while True:
#     if c == 0:
#         break
#     elif c == '+':
#         print(a + b)
#     elif c == '-':
#         print(a - b)
#     elif c == '*':
#         print(a * b)
#     elif c == '/':
#         if b != 0:
#             print(a / b)
#         else:
#             print('делить на ноль нельзя')
# import random
# a = random.randint(1, 10)
# b = random.randint(1, 2)
# print(a)
# print(b)
# i = 0
# while i < 5:
#     c = int(input('введите число '))
#     d = int(input('введите цветЖ 1 красный, 2 черный '))
#     if c > a:
#         print('число меньше ')
#         if d == b:
#             print('но вы угадали цвет')
#         else:
#             print('вы не угадали цвет ')
#     elif c < a:
#         print('число больше ')
#         if d == b:
#             print('но вы угадали цвет')
#         else:
#             print('вы не угадали цвет ')
#     elif c == a and d != b:
#         print('вы не угадали цвет, но угадали число')
#     elif c == a and d == b:
#         print('вы угадали ', a, b)
#         break
# if i < 5:
#     print('попробуй еще раз ')
# else:
#     print('это было число ', a, b, 'игра окончена')
