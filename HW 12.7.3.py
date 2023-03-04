per_cent = {"ТКБ" : 5.6,
            "СКБ" : 5.9,
            "ВТБ" : 4.28,
            "СБЕР" : 4.0}

money = int(input("Введите сумму, которую хотите положить под проценты: "))

ТКБ = round((float(per_cent["ТКБ"])*money/100))
СКБ = round((float(per_cent["СКБ"])*money/100))
ВТБ = round((float(per_cent["ВТБ"])*money/100))
СБЕР = round((float(per_cent["СБЕР"])*money/100))

deposit = [ТКБ, СКБ, ВТБ, СБЕР]

print(deposit, "-Накопленные средства за год вклада")

print(max(deposit), "-Максимальная сумма, которую Вы сможете заработать")
