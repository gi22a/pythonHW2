# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
import random

# 0 = решко, 1 = орёл (орел и решко = heads and tails)
coin_num = int(input("Сколько монеток: "))
coin = []

for i in range(coin_num):
    coin.append(random.randint(0, 1))
# print(coin)
count_heads = 0
count_tails = 0 
for i in coin:
    if i == 0:
        count_tails += 1
    if i == 1:
        count_heads += 1

if count_heads > count_tails:
    print(f"Переерните {count_tails} монет, чтобы все лежали вверх орлом")
else:
    print(f"Переерните {count_heads} монет, чтобы все лежали вверх решком")
    