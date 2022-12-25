money = input("Введите сумму вклада: ")
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
deposit.append(float(per_cent['ТКБ']) * float(money) / 100)
deposit.append(float(per_cent['СКБ']) * float(money) / 100)
deposit.append(float(per_cent['ВТБ']) * float(money) / 100)
deposit.append(float(per_cent['СБЕР']) * float(money) / 100)
print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать - ", max(deposit))
