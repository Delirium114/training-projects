# Проект будильник - начат 11 мая на Макбук в Минеральных водах - Санаторий Елизавета

import datetime
import time

alarm_time = input("Введите время будильника (в формате ЧЧ:ММ): ")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("Вставай ⏰⏰⏰")
        print("\a")
        break
    time.sleep(1)
