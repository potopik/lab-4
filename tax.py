def convert2(num2):
    units2 = ("", "одна ", "две ", "три ", "четыре ", "пять ", "шесть ", "семь ", "восемь ", "девять ", "десять ",
              "одиннадцать ", "двенадцать ", "тринадцать ", "четырнадцать ", "пятнадцать ", "шестьнадцать ",
              "семнадцать ", "восемнадцать ", "девятьнадцать ")
    tens2 = ("", "", "двадцать ", "тридцать ", "сорок ", "пятьдесят ",
             "шестьдесят ", "семьдесят ", "восемьдесят ", "девяносто ")
    hundreds2 = ("", "сто ", "двести ", "тристо ", "четыресто ", "пятьсот ",
                 "шестьсот ", "семьсот ", "восемьсот ", "девятьсот ")
    if num2 < 20:
        return units2[num2]
    if num2 < 100:
        return tens2[num2 // 10] + units2[int(num2 % 10)]
    if num2 < 1000:
        return hundreds2[num2 // 100] + convert2(int(num2 % 100))


def convert(num):
    units = ("", "один ", "два ", "три ", "четыре ", "пять ", "шесть ", "семь ", "восемь ", "девять ", "десять ",
             "одиннадцать ", "двенадцать ", "тринадцать ", "четырнадцать ", "пятнадцать ", "шестьнадцать ",
             "семнадцать ", "восемнадцать ", "девятьнадцать ")
    units1 = ("", "одна ", "две ", "три ", "четыре ")
    tens = ("", "", "двадцать ", "тридцать ", "сорок ", "пятьдесят ",
            "шестьдесят ", "семьдесят ", "восемьдесят ", "девяносто ")
    hundreds = ("", "сто ", "двести ", "тристо ", "четыресто ", "пятьсот ",
                "шестьсот ", "семьсот ", "восемьсот ", "девятьсот ")
    d = (num // 1000) % 10
    if num < 20:
        return units[num]
    if num < 100:
        return tens[num // 10] + units[int(num % 10)]
    if num < 1000:
        return hundreds[num // 100] + convert(int(num % 100))
    if num < 10000:
        if num < 2000:
            return units1[num // 1000] + "тысяча " + convert(int(num % 1000))
        if num < 5000:
            return units1[num // 1000] + "тысячи " + convert(int(num % 1000))
    if 20000 < num < 1000000 and d == 1:
        return convert2(num // 1000) + "тысяча " + convert(int(num % 1000))
    if 20000 < num < 100000 and 5 > d > 1:
        return convert2(num // 1000) + "тысячи " + convert(int(num % 1000))
    if 120000 < num < 1000000 and 5 > d > 1:
        return convert2(num // 1000) + "тысячи " + convert(int(num % 1000))
    if 120000 < num < 1000000 and d == 1:
        return convert2(num // 1000) + "тысяча " + convert(int(num % 1000))
    if num < 1000000:
        return convert2(num // 1000) + "тысяч " + convert(int(num % 1000))


def Bubl(a):
    i=0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        i += 1


n = int(input("Введите количество сотрудников в компании (от 1 до 1000): "))
km = list(map(int, input("Введите расстояние до дома сотрудников в километрах, используя пробел: ").split()))
tarif = list(map(int, input("Введите тарифы такси за проезд одного километра, используя пробел: ").split()))
summa = 0
skm = sorted(km)
starif = sorted(tarif, reverse=True)
for k in range(n):
    summa += starif[k]*skm[k]
for i in range(n):
    km[i] = (km[i], i + 1)
for i in range(n):
    tarif[i] = (-tarif[i], i + 1)
Bubl(km)
Bubl(tarif)
ans = [0] * (n + 1)
for i in range(n):
    ans[km[i][1]] = tarif[i][1]
for i in range(1, n + 1):
    print('Сотрудник №{} должен сесть в такси под номером: '.format(i), ans[i],)
print('Необходимая сумма для оплаты такси:')
print(summa)
b = convert(summa)
if ((summa % 100) > 10) and ((summa % 100) < 15):
    print(b, "рублей")
elif summa % 10 == 1:
    print(b, "рубль")
elif ((summa % 10) > 1) and ((summa % 10) < 5):
    print(b, "рубля")
else:
    print(b, "рублей")