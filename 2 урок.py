# a = 3
# if a > 1:
#     print('a > 1')
# if True:
#     print('Hello')
# a = 2
# if a < 1:
#     print('a < 1')
# else:
#     print('a > 1')
# a = int(input('введи число'))
# if a % 2 == 0:
#     print('четное')
# else:
#     print('нечетное')
# a = int(input('введите число'))
# if  a < 0:
#     print('число меньше 0')
# elif a == 0:
#     print('число равно 0')
# else:
#     print('число больше 0')
# a = int(input('число'))
# b = int(input('число'))
# if a > 0 and b < 0:
#     print('and')
# elif a > 0 or b < 0:
#     print('or')
# a = int(input('первое число'))
# b = int(input('второе число'))
# c = int(input('третье число'))
# if a > b and a > c:
#     print('большее', a)
# elif a < b and b > c:
#     print('большее', b)
# else:
#     print('большее', c)
# a = float(input('ввести первое число'))
# b = str(input('ввести действие'))
# c = float(input('ввести второе число'))
# if b == "+":
#     print(a + c)
# elif b == "-":
#     print(a - c)
# elif b == "*":
#     print(a * c)
# elif b == "/":
#     print(a / c)
# while True:
#     a = int(input('введите год'))
#     if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#         print('высокосный')
#     else:
#         print('не высокосный')
# a = int(input("сторона А"))
# b = int(input("сторона В"))
# c = int(input("сторона С"))
# if (c**2 == a**2 + b**2) or (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2):
#     print("прямоугольный треугольник")
# elif (c == a) and (c + a < b) or (b == a) and (b + a < c):
#     print("тупой треугольник ")
# elif (c != a) and (c!= b) and (a != b):
#     print("остроугольный треугольник")
# else:
#     print("треугольника не существует")
# while True:
#     a = int(input("Введите первую сторону треугольника - "))
#     b = int(input("Введите вторую сторону треугольника - "))
#     c = int(input("Введите третью сторону треугольника - "))
#     if a < b +c and b < a + c and c < a + b:
#         print("\nТреугольник существует")
#         if a == b == c:
#             print("\nТреугольник равносторонний\n")
#         elif a != b and b != c and c != a:
#             print("\nТреугольник разносторонний\n")
#         else:
#             print("\nТреугольник равнобедренный\n")
#     else:
#         print("\nТреугольника не получится\n")
#     break
 