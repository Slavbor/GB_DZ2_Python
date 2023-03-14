# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random
reshka = 0
orel = 0
coin = int(input("Введите количество монет: "))
for i in range(coin):
    storona = random.randint(0, 1)
    if storona == 0:
        orel +=1
    if storona == 1:
        reshka +=1
print(f"Решкой вверх лежат {reshka} мон., орлом вверх лежат {orel} мон.")
if reshka > orel:
    print(f"Нужно перевернуть {orel} мон.")
else:
    print(f"Нужно перевернуть {reshka} мон.")
