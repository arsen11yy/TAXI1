# -*- coding: utf8 -*-

def cost_to_words(n):
    # записть числа словами
    f = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    o = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
         50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
         80: 'восемьдесят', 90: 'девяносто'}
    s = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
         14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
         17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    d = {100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста',
         500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот',
         800: 'восемьсот', 900: 'девятьсот'}
    n1 = n % 10
    n2 = n - n1
    n3 = n-n%100
    result = ""
    # составляем запись числа
    if n3 in d:
        result += d.get(n3) + " "
    if n2 in s:
        result += s.get(n2) + " "
    if n2 in o:
        result += o.get(n2) + " "
    if n1 in f:
        result += f.get(n1) + " "

    # указание валюты
    if str(n)[-1] == '0' or str(n)[-1] == '5' or str(n)[-1] == '6' or str(n)[-1] == '7' or str(n)[-1] == '8' or str(n)[-1] == '9':
        result += "рублей"
    elif str(n)[-1] == '1':
        result += "рубль"
    else:
        result += "рубля"

    return result

def main():
    # целое число - кол-во сотрудников
    print("введите кол-во сотрудников: ")
    number_of_employees = int(input())
    # строку чисел, разделенных пробелом, разделяем и записываем в список, как целые числа
    print("введите расстояния: ")
    distances = list(map(int,input().split()))
    print("введите тарифы: ")
    tariff = list(map(int,input().split()))

    # в списках будем хранить кортеж(расстояние\тариф, номер такси\сотрудника)
    for i in range(number_of_employees):
        distances[i] = (distances[i], i + 1)
    for i in range(number_of_employees):
        tariff[i] = (tariff[i], i + 1)

    # сортируем список
    distances.sort()
    tariff.sort()
    # переворачиваем
    tariff.reverse()

    result = [0] * (number_of_employees + 1)
    summa = 0

    # даем самое такси с самым дешевым тарифом сотруднику с самым длинным путем 
    for i in range(number_of_employees):
        result[distances[i][1]] = tariff[i][1]

        # считаем сумму
        summa += distances[i][0]*tariff[i][0]

    # выводим номера такси
    for i in range(1, number_of_employees + 1):
        print(result[i], end='\n')

	# печатаем сумму в виде числа и в виде строки
    print(summa, end='\n')
    print(cost_to_words(summa))
    
        
main()
