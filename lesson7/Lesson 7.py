# 1,2,3 Делал дз в pycharm  там авторефакторинг PEP

# Задание 4  Подключить библиотеку os. С её помощью вывести: имя операционной системы; имя пользователя, вошедшего в
# терминал; список файлов и директорий в папке.

import os

print(f'Имя вашей операционной системы: {os.name}')
print(f'Имя пользователя: {os.getlogin()}')
print(
    f'В данный момент вы находитесь в директории: {os.getcwd()}. Файлы  в текущей директории: {os.listdir(path=".")}')

# Задание 5, 6, 7 (сравнение установленных библиотек на скриншотах)

import numpyfunctionmodule as np_func

np_func.matrix_function(3, 3)
