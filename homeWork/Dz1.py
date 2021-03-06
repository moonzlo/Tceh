'''
Требования:
Программа выводить в консоль текст загадки и ждать ввода пользователя
Программа после ввода пользователя ответа должна вывести в консоль результат: правильный ли ответ дал пользователь
Загадок должно быть 10, тематика вопросов должна быть по первому занятию
'''

otvetov = [0]
oshibok = [0]
while True:
    zadanie1 = input('Для преобразования числа в строку выполните "___(100)')
    if zadanie1 in 'str, Str, STR':
        print('Верно')
        otvetov[0] += 1
        break
    else:
        print('Не верно')
        oshibok[0] += 1

while True:
    zadanie2 = input('Для преобразования строки в число выполните "___(100)')
    if zadanie2 in 'int, Int, INT':
        print('Верно')
        otvetov[0] += 1
        break
    else:
        print('Не верно')
        oshibok[0] += 1

while True:
    zadanie3 = input('Какой тип данных будет у переменной f, если f = 12 + 2.5?')
    if zadanie3 in 'float, Float. FLOAT':
        print('Верно')
        otvetov[0] += 1
        break
    else:
        print('Не верно')
        oshibok[0] += 1
while True:
    zadanie4 = input('Как в Python обозначается истина?')
    if zadanie4 in 'true, True, TRUE':
        print('Отлично!')
        otvetov[0] += 1
        break
    else:
        print('Не верно!')
        oshibok[0] += 1

print('Правельных ответов: {}| Ошибок: {}'.format(otvetov[0], oshibok[0]))

'''
ДОП ЗАДАНИЯ: 
1)Напишите программу, которая считает площадь прямоугольника, спрашивая у пользователя длину двух сторон.
2)Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-". В зависимости от знака выводит 
их сумму или разницу.
3)Напишите программу, которая находит все простые числа между 0 и пользовательским числом.
4)Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами.
'''

# Task 1 Напишите программу, которая считает площадь прямоугольника, спрашивая у пользователя длину двух сторон

side_a = input('Введите длину стороны А прямоугольника: ')
side_b = input('Введите длину стороны B прямоугольника: ')

print('Площадь прямоугольника: ', int(side_a) * int(side_b))

# Task 2 Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-".
# В зависимости от знака выводит их сумму или разницу
num1 = float(input('Введи первое число: '))
num2 = float(input('Введи второе числов:'))
while True:
    symbvol = str(input('Введи "+" или "-"'))
    if symbvol == '+':
        print(num1 + num2)
        break
    elif symbvol == '-':
        print(num1 - num2)
        break
    else:
        print('Вы ввели что-то другое')
        continue

# Task 3 Напишите программу, которая находит все простые числа между 0 и пользовательским числом.

'''
Да я тупой, и НЕ ПОНИМАЮ что такое простые числы, пробовал почтитать но ничего не понял....
'''
# НЕ МОЁ РЕШЕНИЕ
# введем число, заранее знаем, что оно должно быть типа int
print('Задание 1:   \nРасчитываем все простые числа от 0 до выбранного Вами числа\n')
limit = int(input('Введите число: '))

numbers = list()

# обойдем все числа от 2 до указанного числа + 1
for n in range(2, limit + 1):
    # обойдем все числа от 2 до текущего числа в обходе
    for m in range(2, n):
        # если делится без остатка то число НЕ простое - прерываем внутренний цикл для перехода к след. числу
        if n % m == 0:
            break
    else:
        # в противном случае оно простое и добавляем его в список
        numbers.append(n)

print(numbers)

# Task 4 Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами

# вводим два числа типа int так как должны быть кратны 5
print('\n\nЗадание 2:   \nНайдем все числа в заданном 2 числами диапазоне кратные 5\n')
num1 = int(input('Введите 1ое число: '))
num2 = int(input('Введите 2ое число: '))

numbers = list(x for x in range(num1, num2) if x % 5 == 0)
print(numbers)