# def a():
#     sum = 0
#     for i in range(10):
#         sum += i
#     print(sum)
# a()
# def add(a, b):
#     return a + b
# print(add(1, 2))
# a = int(input('введите число '))
# b = int(input('введите число '))
# if a - b == 135 or b - a == 135:
#     print('yes')
# else:
#     print('no')
# from random import randint
# a = randint(-200, 200)
# print(a)
# if a >100 or a < -100:
#     print('-')
# else:
#     print('+')
# a = 0
# b = 0
# for i in range(3):
#     c = int(input('введите число '))
#     if c > 0:
#         a += 1
#     elif c < 0:
#         b += 1
# print(a, 'положительных и', b, 'отрицательных')
# a = 0
# while a <= 100:
#     a = int(input('введите число '))
#     if a > 100:
#         break
#     elif a < 10:
#         continue
# print(a)
# while True:
#     a = int(input('введите число '))
#     if a < 10:
#         continue
#     elif a > 100:
#         break
#     else:
#         print(a)
# a = [1, 2, -5, 6, -8, -2, 55, 64, -6, 122]
# b = []
# for i in a:
#     if i > 0 and i % 2 == 0:
#         b.append(i)
# print(b, 'сумма четных чисел ', sum(b))
# a = int(input('введите число '))
# b = int(input('введите число '))
# a1 = 0
# b1 = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         a1 += i
#         b1 += 1
# print(a1 / b1)
# a = int(input('введите число '))
# b = 0
# while a != 0:
#     b = b + a % 10
#     a = a // 10
# print(b)
# a = str(input('введите текст '))
# while True:
#     if len(a) >= 10:
#         print('!!!')
#         break
#     elif len(a) < 10:
#         print(a[1])
#         break
