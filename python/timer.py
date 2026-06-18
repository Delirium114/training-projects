# Таймер обратного отсчета - проект начат 01.05.2025г
import time

input_second = int(input('Введите количество секунд: '))

if input_second < 1:
    print('Введите положительное число')

while input_second != 0:
    if input_second == 1:
        print(f'Осталось: {input_second} секунда')
        input_second = input_second - 1
        time.sleep(1)
        print('⏰ Время вышло!')
        print('\a')

    else:
        print(f'Осталось: {input_second} секунд')
        time.sleep(1)
        input_second = input_second - 1