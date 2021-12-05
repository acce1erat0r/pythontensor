#Задание 1
ArrCount = int(input("Введите количество элементов в массиве, который хотите отсортировать: "))
listBeforeBuble = []

for i in range(arrCount):
    listBeforeBuble.append(int(input("Введите число: ")))

for i in range(0, len(listBeforeBuble) - 1):
    for j in range(len(listBeforeBuble) - 1):
        if (listBeforeBuble[j] > listBeforeBuble[j + 1]):
            listBeforeBuble[j], listBeforeBuble[j + 1] = listBeforeBuble[j + 1], listBeforeBuble[j]

print(listBeforeBuble)

# Задание 2

color = {'Red': (255, 0, 0),
         'Pink': (255, 192, 203),
         'Orange': (255, 165, 0),
         'Yellow': (255, 255, 0),
         'Violet': (238, 130, 238),
         'Black': (0, 0, 0),
         'White': (255, 255, 255)}

print(color['Red'])

# Задание 3

import random

listNumbersOne = []
listNumbersTwo = []


def fillListRandomNumbers(someList):
    for i in range(0, 10):
        someList.append(random.randrange(0, 10))

    return someList


fillListRandomNumbers(listNumbersOne)
fillListRandomNumbers(listNumbersTwo)

print(listNumbersOne)
print(listNumbersTwo)

# 1 task
tmpSetOne = set(listNumbersOne)
tmpSetTwo = set(listNumbersTwo)
intersectionOfLists = tmpSetOne.intersection(tmpSetTwo)
print(f' Пересечение множеств: {intersectionOfLists}')

# 2 task
individualNumbersForOneSet = tmpSetOne.difference(tmpSetTwo)
print(f' Числа содержащиеся только в первом множестве: {individualNumbersForOneSet}')

# 3 task
individualNumbersForTwoSet = tmpSetTwo.difference(tmpSetOne)
print(f' Числа содержащиеся только во втором множестве: {individualNumbersForTwoSet}')

# 4 task
individualNumbersFromOneAndTwoSet = individualNumbersForOneSet.union(individualNumbersForTwoSet)
print(f' Числа входящие в первое или во второе множества, но не в оба одновременно: {individualNumbersFromOneAndTwoSet}')



