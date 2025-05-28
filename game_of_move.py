#Проект игра в кости - начата 28 мая 2025 года сидя в It  клубе

import random
import time

def roll_dice():
    """Функция отвечает за имитацию броска кубика и подсчет очков"""

    first_cube = random.randint(1,6)
    second_cube = random.randint(1,6)
    total_score = first_cube + second_cube

    print(f"{first_cube} и {second_cube} = {total_score}\n")
    return total_score


# Основной цикл программы

check_user = 0
check_computer = 0

while check_user != 3 or check_computer != 3:

    print("Добро пожаловать в игру 'Бросай кости'\n")
    print('Вы первым будете бросать кости\n')
    input("Нажмите Enter, чтобы бросить кости 🎲...")
    print('Бросаем кубики')
    time.sleep(2)
    user_cube = roll_dice() #Присваиваем значение игроку

    print("Компьютер бросает кубики")
    time.sleep(3)
    computer_cube = roll_dice() # Присваиваем значение компьютеру

    if user_cube > computer_cube:
        print('Поздравляем вы выйграли\n')
        check_user += 1

    elif computer_cube > user_cube:
        print('Компьютер выйграл!!!')
        check_computer += 1

    else:
        print("Ничья")


    again_game = input('Хотите сыграть еще раз: ').lower()

    if not again_game.startswith('д'):
        print("До встречи")
        break
