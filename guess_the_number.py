# Игра поиск чисел - Проект начат 03.05.2025г

import random

print("Добро пожаловать в программу по поиску цифр")
print('Программа загадает число, твоя задача угадать число с трех пяти попыток')

attempt = 1

# генерация случайного числа
last_digit = 10



# Пользователь вводит уровень
user_input_level = int(input('В каком диапазоне ты хочешь поискать цифру:\n1)от 1 до 10\n2)от 1 до 50\n3)от 1 до 100\nУровень номер: '))

if user_input_level == 1:
    print("Отлично! Ты выбрал первый уровень - самый легкий. Он идеально подойдет для начала ✯")
    last_digit = 10
elif user_input_level == 2:
    print("Ты выбрал большой диапазон, будет сложновато. Твой - уровень ✯✯")
    last_digit = 50
elif user_input_level == 3:
    print("Самый сложный выбор! Держу за тебя кулачки - ✯✯✯")
    last_digit = 100

random_digit = random.randint(1,last_digit)
print(f"\nПрограмма загадала цифру от 1 до {last_digit}. Какую цифру ты введешь: ")

#user_input_digit = int(input())

while attempt < 5 :

    user_input_digit = int(input(f"Попытка № {attempt}: "))

    if user_input_digit > random_digit:
        print('Твое число больше, попробуй поменьше')
    elif user_input_digit < random_digit:
        print('Твое число меньше. Попробуй взять побольше')
    else:
        print('Ура! Ты угадал. Ты большой молодец!')

        if attempt == 1:
            print(f"Тебе понадобилось всего {attempt} попытка")
        elif 1 < attempt < 5:
            print(f"Ты угадал за {attempt} попытки")
        else:
            print(f'Тебе понадобилось {attempt} попыток')

        break

    attempt += 1

if attempt >= 5:
    print(f'\nК сожалению ты не смог отгадать. Было загадано число - {random_digit}')