# Контекстные менджеры


from contextlib import contextmanager

'''

+1. Дан класс:
    class Lock(object):
      def __init__(self):
        self.lock = False
    
    Сделать менеджер контекста, который может переопределить 
    значение lock на True внутри блока контекста.
'''
# @contextmanager
# def editor(obj):
#     item = obj
#     yield item
#     obj.lock = False
#     print('Состояние lock', obj.lock)
#
# class Lock(object):
#     def __init__(self):
#         self.lock = False
#
#
# a = Lock()
# with editor(a) as obj:
#     obj.lock = True
#     print(obj.lock)
#
# print(a.lock)

'''
+2. Сделать менеджер контекста, который бы проглатывал все исключения вызванные 
   в теле и писал их в консоль, пример использования:
    
    with no_exceptions():
      1 / 0 # => logs: ZeroDivisionError

    print('Done!') # => continues execution
'''
# @contextmanager
# def no_exceptions():
#     try:
#         yield print('Ловим исключение')
#     except Exception as error:
#         print(error)
#
# with no_exceptions():
#     print(1/0)
#     print('Okay')

'''
+3. Сделать менеджер контекста, который бы мог измерять время выполнения блока кода, 
   пример использования:
    
    with TimeIt() as t:
      some_long_function()

    print('Execution time was:', t.time)
'''
# import time
#
# def some_long_function():
#     time.sleep(2)
#
# @contextmanager
# def TimeIt():
#     start = time.time()
#     yield print('работаю')
#     print(time.time() - start)
#
# with TimeIt():
#     some_long_function()