# генератор паролей - проект начат 29.04.2025г.
import random

eng_letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'

eng_lower_letters = eng_letters.replace(' ','')
eng_upper_letters = eng_lower_letters.upper()
digits = '1234567890'

password_char = ''

#---
lenght_password = int(input("Введите длину пароля: "))

uppper_letters_input = input("Хотите ли вы включить заглавные буквы: ").lower()
if uppper_letters_input.startswith('д'):
    password_char = password_char + eng_upper_letters

lower_letters_input = input("Хотите ли вы включить строчные буквы: ").lower()
if lower_letters_input.startswith('д'):
    password_char = password_char + eng_lower_letters

digits_input = input('Хотите ли вы включить цифры в свой пароль: ').lower()
if digits_input.startswith('д'):
    password_char = password_char + digits

print()
print('Ваш пароль: ',end='')

for i in range(lenght_password):
    password = random.choice(password_char)
    print(password,end='')

