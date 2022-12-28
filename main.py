import random

user = 0
ai = 0

while user < 5:
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
        user = user + 1
        print(f'{c} ты победил!, user-{user}: ai-{ai}')

    elif a == 'камень' and c == 'бумага':
        ai = ai + 1
        print(f'{c} ты проиграл!, user-{user}: ai-{ai}')

    elif a == 'ножницы' and c == 'камень':
        ai = ai +  1
        print(f'{c} ты проиграл!, user-{user}: ai-{ai}')

    elif a == 'ножницы' and c == 'бумага':
        user = user + 1
        print(f'{c} ты выиграл!, user-{user}: ai-{ai}')

    elif a == 'бумага' and c == 'камень':
        user = user + 1
        print(f'{c} ты выиграл!, user-{user}: ai-{ai}')

    elif a == 'бумага' and c == 'ножницы':
        ai = ai + 1
        print(f'{c} ты проиграл!, user-{user}: ai-{ai}')
