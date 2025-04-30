# генератор паролей - проект начат 29.04.2025г.
import random

eng_letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'

eng_lower_letters = eng_letters.replace(' ','')
eng_upper_letters = eng_lower_letters.upper()
digits = '1234567890'

password_char = ''

#-----------------------------------------------------------------------------#
length_password = int(input("Введите длину пароля: "))


upper_letters_input = input("Хотите ли вы включить заглавные буквы (да/нет): ").lower()
if upper_letters_input.startswith('д'):
    password_char = password_char + eng_upper_letters

lower_letters_input = input("Хотите ли вы включить строчные буквы (да/нет): ").lower()
if lower_letters_input.startswith('д'):
    password_char = password_char + eng_lower_letters

digits_input = input('Хотите ли вы включить цифры в свой пароль (да/нет): ').lower()
if digits_input.startswith('д'):
    password_char = password_char + digits

if not password_char:
    print("Вы не выбрали ни одного типа символов для пароля. Завершение программы.")
    exit()

print()
print('Ваш пароль: ',end='')

for i in range(length_password):
    password = random.choice(password_char)
    print(password,end='')

