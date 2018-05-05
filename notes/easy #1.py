# BorisRubin
# https://github.com/BorisRubin/TCEH-Homeworks/blob/master/Homework7/Main/main.py

from functools import wraps, reduce
from time import time

# ДЕКОРАТОРЫ
# @wraps(f) используется для сохранения контекста декорируемой функции в декораторе
# например для вывода имени декорируемой функции
def canceler(func):
    """
    Декоратор отменяющий выполнение любой декорированной функции и выводит сообщение в консоль
    """
    @wraps(func)
    def cancel_wrap(*args, **kwargs):
        return '{} is canceled!'.format(func.__name__)

    return cancel_wrap


def timer(func):
    """
    Декоратор замеряющая время выполнение любой декорированной функции
    """
    @wraps(func)
    def timer_wrap(*args, **kwargs):
        start = time()
        func_return = func(*args, **kwargs)
        end = time()
        print('{} is working for {} seconds'.format(func.__name__, (end-start)))
        return func_return

    return timer_wrap


def logger(func):
    """
    Декоратор логирующая выполнение любой декорированной функции
    """
    print('Decorator created\n')

    @wraps(func)
    def logger_wrap(*args, **kwargs):


        print('\n1.\'{}\' started\n'.format(func.__name__))
        func_return = func(*args, **kwargs)
        print('2.\'{}\' stopped\n'.format(func.__name__))

        return func_return

    return logger_wrap


def catcher(func):

    @wraps(func)
    def catcher_wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return 'Exception \'{}\' occured while running \'{}\''.format(e, func.__name__)
    return catcher_wrap


class Counter(object):
    """
    Класс счетчик со стичным методом декоратором для счетчика вызовов любой декорированной функции
    в instances хранится словарь с функциями и кол-вом их вызовов
    """

    instances = {}

    @staticmethod
    def call_counter(func):

        def counter_wrap(*args, **kwargs):

            if func.__name__ in Counter.instances.keys():
                Counter.instances[func.__name__] += 1
            else:
                Counter.instances[func.__name__] = 1

            print('{} is called {} times'.format(func.__name__, Counter.instances[func.__name__]))

            return func(*args, **kwargs)

        return counter_wrap



# ОРИГИНАЛЬНЫЕ ФУНКЦИИ
@Counter.call_counter
@canceler
def long(value):
    import time
    time.sleep(5) # delays for 5 seconds

    return 'long_' + str(value)

@Counter.call_counter
@logger
def short(string_param):
    print('Speed!', string_param)
    return 'short'

@Counter.call_counter
@timer
def medium(value, *modificators):
    result = value
    for m in modificators:
        result *= m

    return result

@Counter.call_counter
@catcher
def change_sign(num, check_sign=True):
    if check_sign and num > 0:
        raise ValueError('num > 0!')
    return -num



# ОСНОВАЯ ФУНКЦИЯ МОДУЛЯ
def main():

    print('***** TASK 7 part 1 *** Decorators ***\n')
    print(long(300))
    print(long(3))
    print(long(14))
    print(long(1))
    print('\n*************************')


    print('\n*************************')
    print(medium(1,2,3,4,5,6,7,8,9,10))
    print(medium(1,2,3,4,5,6,7))

    print('\n*************************')
    print(short('Hi'))
    print(short('Bye'))

    print('\n*************************')
    print(change_sign(15, True))
    print(change_sign(15, False))
    print(change_sign(-115, True))

    print('\n*************************')


    print('***** TASK 7 part 2 *** Map/Filter/Reduce/Lambda ***\n')
    # При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
    print('map result:', list(map(lambda x: x % 5, [1, 4, 5, 30, 99])))
    # При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
    print('map result:', list(map(str, [3, 4, 90, -2])))
    # При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки
    print('filter result:', list(filter(lambda s: not isinstance(s, str), ['some', 1, 'v', 40, '3a', str])))
    # При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']
    print('reduce result:', reduce(lambda a, b: a + b, list(len(x) for x in ['some', 'other', 'value'])))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')