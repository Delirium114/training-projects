# Проект список дел - начат на работе в серверной в Грозном 13/05/2025
# Программа закончена в 14 мая

def show_display():
    """Функция отвечает за отображения меню программы"""
    print('1 ➕ Добавить задачу')
    print('2 📖 Показать все задачи')
    print('3 🗑 Удалить задачу')
    print('4 ❌ Выйти\n')

def add_notes():
    """Функция отвечает за добавление заметок в файл"""
    input_note = input("Введите заметку, которую хотите добавить: ")
    with open("todo.txt", "a", encoding="utf-8") as file:
        file.write(input_note + '\n')
    print("✅ Заметка добавлена\n")


def show_notes():
    """Функция отвечает за показ заметок"""
    try:
        with open("todo.txt", "r", encoding="utf-8") as file:
            content = file.readlines()

        if not content:
            print('Здесь пока нет записей')

        else:
            print('Вот ваши записи:')
            for i,note in enumerate(content, start=1):
                print(f'{i}. {note.strip()}')
            print()

    except FileNotFoundError:
        print('Файл пока не создан')


def deleted_task():
    """Для удаления задач используется данная функция"""

    try:
        with open("todo.txt", "r", encoding="utf-8") as file:
            content_deleted = file.readlines()

        if not content_deleted:
            print('Здесь пока нет записей')
            return

        else:
            print('Все записи: ')
            for i, note in enumerate(content_deleted, start=1):
                print(f'{i}. {note.strip()}')
            print()
            number_task = input('Введите номер задачи, которую нужно удалить: ')
            print()
        if not number_task.isdigit():
            print('Нужно ввести число: ')
            return

        number_task = int(number_task)
        if 1 <= number_task <= len(content_deleted):
            deleted_tasks = content_deleted.pop(number_task - 1)

            with open("todo.txt", "w", encoding="utf-8") as file:
                file.writelines(content_deleted)

            print(f"✅ Удалена задача: {deleted_tasks.strip()}\n")

        else:
            print('❗ Такого номера нет.\n')

    except FileNotFoundError:
        print('❗ Файл со списком задач пока не создан.\n')


#Показывает дисплей
show_display()

while True:

    user_choice = input('Что вы хотите сделать: ')

    if user_choice == '1':
        add_notes()

    elif user_choice == '2':
        show_notes()

    elif user_choice == '3':
        deleted_task()

    elif user_choice == '4':
        print('До свидания!')
        break

    else:
        print('Введите число')