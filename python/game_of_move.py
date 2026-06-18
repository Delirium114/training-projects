#Проект игра в кости - начата 28 мая 2025 года сидя в It клубе

import random
import time

def roll_dice():
    """Функция отвечает за имитацию броска кубика и подсчет очков"""

    first_cube = random.randint(1,6)
    second_cube = random.randint(1,6)
    total_score = first_cube + second_cube

    print(f"{first_cube} и {second_cube} = {total_score}\n")
    return total_score


def display():
    """Функция отображает приветственное окно"""
    print("Добро пожаловать в игру 'Бросай кости'\n")
    input("Нажмите Enter, чтобы бросить кости 🎲...\n")
    print('Игра началась\n')


def main_loop():
    """Функция для основной """

    check_user = 0
    check_computer = 0

    while check_user != 3 and check_computer != 3:

        print('Ты бросаешь кубики')
        time.sleep(2)
        user_cube = roll_dice()  # Присваиваем значение игроку

        print("Компьютер бросает кубики")
        time.sleep(2)
        computer_cube = roll_dice()  # Присваиваем значение компьютеру

        if user_cube > computer_cube:
            check_user += 1
        elif computer_cube > user_cube:
            check_computer += 1

        # вывод счета на каждой итерации
        if check_user > check_computer:
            print(f"Общий счет {check_user}:{check_computer} в твою пользу\n")
            if check_user == 3:
                print('Ты выйграл! Поздравляю!')
        elif check_computer > check_user:
            print(f"Общий счет {check_user}:{check_computer} в пользу компьютера\n")
            if check_computer == 3:
                print('На этот раз удача была на стороне компьютера!')
        else:
            print(f'У нас пока ничью. Счет {check_user}:{check_computer}')


# Начало программы
display() # Вывод приветственного окна
main_loop() # Основная программа

while True:
    play_again = input('Хотите сыграть еще раз: ').lower()

    if play_again.startswith('д'):
        print('Мы начинаем заново')
        main_loop()

    else:
        print("Продолжим наши баталии в следующий раз")
        break
