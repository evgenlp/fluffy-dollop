import random

while True:
    a = input('камень, ножницы, бумага :')
    b = random.randint(1, 3)
    c = ''
    if b == 1:
        c = 'камень'
    elif b == 2:
        c = 'ножницы'
    elif b == 3:
        c = 'бумага'
    if a == c:
        print(f'{c}: ничья, пробуй еще раз')
    elif a == 'камень' and c == 'ножницы':
        print(f'{c} ты победил!')
        # break
    elif a == 'камень' and c == 'бумага':
        print(f'{c} ты проиграл!')
        # break
    elif a == 'ножницы' and c == 'камень':
        print(f'{c} ты проиграл!')
        # break
    elif a == 'ножницы' and c == 'бумага':
        print(f'{c} ты выиграл!')
        # break
    elif a == 'бумага' and c == 'камень':
        print(f'{c} ты выиграл!')
        # break
    elif a == 'бумага' and c == 'ножницы':
        print(f'{c} ты проиграл!')
        # break