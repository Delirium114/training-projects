# Проект Записи в Дневник - начат 12 мая в Грозном ГГКИТ

import datetime

notes = []

def show_display():
    print('Выберите действие:')
    print('1 - Добавить новую заметку')
    print('2 - Посмотреть все заметки')
    print('3 - Удалить')
    print('4 - Выйти')
    print()

def add_notes():

    input_notes = input('Введите свою заметку: ')
    now_time = datetime.datetime.now().strftime("%d.%m.%H:%M")

    full_note = f'{now_time} {input_notes} -- '

    #print()
    notes.append(full_note) # временно сохраняет  пока сессия активна

    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(full_note + '\n')

    print("✅ Заметка добавлена\n")

def show_notes():

    try:
        with open("diary.txt", "r", encoding="utf-8") as file:
           content = file.readlines()

        if not content:
            print('Пока записей нет')

        else:
            print('Все заметки: ')
            for i,note in enumerate(content,start=1):
                print(f"{i} {note.strip()}")
        print()

    except FileNotFoundError:
        print("📂 Файл дневника пока не создан.\n")

def delete_note():

    if not notes:
        print('Пока нет заметок для удаления')
        return

    #show_notes()

    try:
        delete_number = int(input('Введите номер заметки, которую хотите удалить: '))
        if 1 <= delete_number <= len(notes):
            deleted = notes.pop(delete_number-1)
            print(f'Заметка удалена: {deleted}')
        else:
            print('Такой заметки нет')

    except ValueError:
        print('Нужно вести число')


while True:
    show_display()
    choice = input('Какой пункт ты выбираешь: ')
    print()

    if choice == '1':
        add_notes()

    elif choice == '2':
        show_notes()

    elif choice == '3':
        delete_note()

    elif choice == '4':
        print("Удачи!")
        break

    else:
        print('Неправильно выбранный пункт')
