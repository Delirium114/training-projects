#Проект калькулятор с логами - начат в серверной на работе 16 мая

def numbers_and_operation():
    """Функция запрашивает числа и операцию"""

    number_one = int(input('Введите первое число: '))
    number_two = int(input('Введите второе число: '))

    operation = input("Какую операция вы хотите произвести на числами (+ - * %): \n")

    result = 0

    if operation == "+":
        result = number_one + number_two

    elif operation == "-":
        result = number_one - number_two

    elif operation == "*":
        result = number_one * number_two

    elif operation == "%":
        if number_two == 0 or number_one == 0:
            print('Делить на ноль нельзя')
        else:
            result = number_one / number_two

    else:
        print("Введите правильную операцию")
        return None

    with open("calc_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{number_one} {operation} {number_two} = {result} ")
    print('Запись добавлена\n')

    print(f"{number_one} {operation} {number_two} = {result}")
    return f"{number_one} {operation} {number_two} = {result}"

# основной цикл работы

while True:

    print('1-Выполнить вычисление')
    print('2-Показать логи')
    print('3-Очистить логи')
    print('4-Выйти\n')

    choice_input = input('Выберите действия: ')

    if choice_input == "1":
        numbers_and_operation()

    elif choice_input == "2":

        try:
            with open("calc_log.txt", "r", encoding="utf-8") as file:
                print('Запись вычислений: ')
                for i in file:
                    print(i.strip())
                print()

        except FileNotFoundError:
            print('Записей не найдено')

    elif choice_input == "3":
        with open("calc_log.txt", "w", encoding="utf-8") as file:
            pass
        print('Файл с логами был очищен\n')

    elif choice_input == "4":
        print('Всего наилучшего')

    else:
        print('Неверный ввод\n')
