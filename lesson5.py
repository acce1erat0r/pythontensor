# Задание 1

def passwordCreate(password):
    if len(password) > 6:
        flag = False
        for i in password:
            if i.isdigit():
                flag = True
        if flag:
            if not password.isdigit():
                if password.lower().find("password", 0, len(password)) == -1:
                    print('Ваш пароль успешно создан')
                else:
                    print("Ваш пароль слишком слаб, так как содержит в себе слово password")
            else:
                print("Ваш пароль слишком слаб, так как состоит из одних цифр")
        else:
            print("error")
    else:
        print("Ваш пароль слишком короткий, введите пароль больше 6ти символов")


password = input('Введите ваш пароль: ')
passwordCreate(password)


# Задание 2

def sumArgs(*args):
    sumAll = 0
    if len(args) != 0:
        for i in args:
            sumAll += i
        return sumAll
    else:
        return sumAll


print(sumArgs(1,2,3,4,5,6,7,8))


