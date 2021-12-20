"""1)Написать класс “animals” (животные), который включает общие признаки и поведения животных. От “animals”
наследовать класс “mammals” (млекопитающие), который включает общие признаки и поведения млекопитающих. От “mammals”
наследовать “human” (человек), “cat”(кот), “dog”(собака), у каждого свои признаки и поведения.
2)Написать класс
“Student”, который наследует класс human, у которого среди прочих признаков есть “Количество сданных дз”.
3)*
Перегрузить операторы сравнения так, чтобы студенты сравнивались по количеству сданных ими дз.
4)* Написать функцию.
Для неё написать декораторы для следующего функционала:
    ◦ логирование выполнения функции;
    ◦ время выполнения функции;
    ◦ замедлить выполнение кода. Ограничить частоту вызова функции. """

from models import AnimalClass, MammalsClass, HumanClass, CatClass, DogClass, StudentClass

anima = AnimalClass.Animals('Медведь', 'gray', 123)
human = HumanClass.Human('Человек', 'white', 60, True, False)
cate = CatClass.Cat('Кот', 'black', 7, True, False)
Dog = DogClass.Cat('Собака', 'gray', 10, True, False)
student_one = StudentClass.Student('Студент', 'white', 60, 101, True, False)
student_two = StudentClass.Student('Студент2', 'white', 60, 101, True, False)
print(student_one < student_two)
print(student_one > student_two)
print(student_one == student_two)