# Проект будильник - начат 11 мая на Мак"%H:%M")бук в Минеральных водах - Санаторий Елизавета

import datetime
import time

while True:

    alarm_time = input("Введите время будильника (в формате ЧЧ:ММ): ")

    try:
        datetime.datetime.strptime(alarm_time,"%H:%M")
        break

    except ValueError:
        print('Неверный формат времени')


while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("Вставай ⏰⏰⏰")
        print("\a")
        break
    time.sleep(1)
