#Проект калькулятор с логами - начат в серверной на работе 16 мая

def numbers_and_operation():
    """Функция запрашивает числа и операцию"""

    number_one = int(input('Введите первое число: '))
    number_two = int(input('Введите второе число: '))

    operation = input("Какую операция вы хотите произвести на числами (+ - * %): ")

    result = 0

    if operation == "+":
        result = number_one + number_two
        return  print(f"{number_one} + {number_two} = {result} ")

            #return f"{number_one} + {number_two} = {result} "

    elif operation == "-":
        result = number_one - number_two
        return print(f"{number_one} - {number_two} = {result} ")

    elif operation == "*":
        result = number_one * number_two
        return print(f"{number_one} * {number_two} = {result} ")

    elif operation == "%":
        result = number_one / number_two
        return print(f"{number_one} / {number_two} = {result} ")

    else:
        print("Введите правильную операцию")
        return None


    with open("calc_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{number_one} {operation} {number_two} = {result}")

    print('Запись добавлена')

# основной цикл работы

while True:

    print('1-Выполнить вычисление')
    print('2-Показать логи')
    print('3-Выйти')

    choice_input = input('Выберите действия: ')

    if choice_input == "1":
        numbers_and_operation()

    elif choice_input == "2":

        try:
            with open("calc_logs.txt", "r", encoding="utf-8") as file:
                print('Запись вычислений: ')
                print(file.read())

        except FileNotFoundError:
            print('Записей не найдено')

    elif choice_input == "3":
        print('Всего наилучшего')

    else:
        print('Неверный ввод\n')
