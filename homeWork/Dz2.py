'''
Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем

Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
чтобы получилось: 'Earth -> Russia -> Moscow'

Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'

Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет

Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс

Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'

Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль
'''

# Task 1 | Создать лист из 6 любых чисел. Отсортировать его по возрастанию.

list1 = [2, 3, 1, 4, 6, 5]
print(sorted(list1))

# Task 2 | Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно

dict = {1: 'first', 12: 'twelwe', 5: 'five', 6: 'six', 20: 'twenty'}

print('Исходный словарь', dict)
for key, value in dict.items():
    print(key, value)


# Task 4 | Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
# чтобы получилось: 'Earth -> Russia -> Moscow'

words = ['Earth', 'Russia', 'Moscow']
print(" -> ".join(words))

# Task 5 | Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'

stroka = r'/bin:/usr/bin:/usr/local/bin'
print(stroka.split(':'))

# Task 6 | Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7,
# а какие - нет

for i in range(1, 100):
    if i % 7 == 0:
        print('and {} is!'.format(i))
    else:
        print('{} is not multiple of 7'.format(i))

# Task 7 | Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

print('\n\nЗАДАЧА 7: Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы')
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

print('Выводим строки\n')
for col in range(len(matrix)):
    print('\n')
    for string in range(len(matrix[col])):
        print(matrix[col][string], end=' ')

print('Выводим колонки\n')
for string in range(len(matrix[col])):
    print('\n')
    for col in range(len(matrix)):
        print(matrix[col][string], end=' ')

# Task 8 | Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс

obj = [1, 'fix', False, None, {1:'dict'}, (5,6,7)]
for i in obj:
    print(i, ' ', obj.index(i))

# Task 9 | Создать список с тремя значениями 'to-delete'
# и нескольми любыми другими, удалить из него все значения 'to-delete'

spisok = ['one', 'to-delete', 2, 'to-delete', 5, 'to-delete']

for i in spisok:
    if i == 'to-delete':
        spisok.remove(i)
print(spisok)

# Task 10 | Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль

a = range(1,11)
b = []
for i in a:
    b.append(i)
b.reverse()
print(b)