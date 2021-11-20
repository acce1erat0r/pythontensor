#imports
from math import pi

# 1 Task
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

print(f'Вычитание - {number1 - number2}')
print(f'Сложение - {number1 + number2}')
print(f'Умножение - {number1 * number2}')
print(f'Деление - {number1 / number2}')
print(f'Возведение в степень - {number1 ** number2}')
print(f'Деление по модулю - {number1 % number2}')
print(f'Целочисленное деление - {number1 // number2}')

#2 Task
name = input("Введите ваше имя: ")
print(f'Hello {name}')

#3 Task
for i in range(1,3):
    TestString = input("Введите любую строку: ")
    print(TestString[-1:-3:-1])
#Так и не понял что значит решить не более чем две строки, подумал, что речь идет о циклах


#4 Task
rad = float(input("Введите радиус круга: "))
print(f'Площадь круга равна: {pi * rad**2}')
