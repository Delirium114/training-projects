# Проверка пароля - Проект начат 30.04.2025

user_password_input = input("Введите свой пароль: ")

point = 0

has_upper =  any(char.isupper() for char in user_password_input)
has_lower =  any(char.islower() for char in user_password_input)
has_digit =  any(char.isdigit() for char in user_password_input)
has_simbols = any(char in "!@#$%^&*()-_=+[]{};:,.<>/?" for char in user_password_input)
#--------------------------------------------------------------#
if len(user_password_input) >= 8:
    point += 1
if has_upper:
    point += 1
if has_lower:
    point += 1
if has_digit:
    point += 1
if has_simbols:
    point += 1
#---------------------------------------------------------------#
if point > 4:
    print("🔒 Пароль очень надежный")
elif point == 3:
    print("✅ Пароль надежный")
elif point == 2:
    print("⚠️ Пароль нормальный")
else:
    print("❌ Пароль слабый")

print(f"Ваш пароль набрал: {point} баллов")