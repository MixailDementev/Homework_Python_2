# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randint
# 	num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
NUMBER_OF_ATTEMPTS = 10
RAND_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
VICTORY = True
for _ in range(NUMBER_OF_ATTEMPTS):
    number = int(input('Введи число от 0 до 1000: '))
    if number > RAND_NUMBER:
        print('Ваше число БОЛЬШЕ загаданного')
        VICTORY = False
    elif number < RAND_NUMBER:
        print('Ваше число МЕНЬШЕ загаданного')
        VICTORY = False
    else:
        print('Вы выиграли!')
        VICTORY = True
        break
if not VICTORY:
    print('К сожалению вы проиграли')
