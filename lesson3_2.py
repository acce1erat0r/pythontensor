
x = 0
y = 0


def is_number(x, y):
    try:
            int(x)
            int(y)
            return True
    except ValueError:
            return False

while(True):
    stop_command = input("Если хотите завершить программу введите команду <stop>, если нет оставьте это поле пустым: ")


    if(stop_command == "stop"):
        print("Вы решили завершить программу.")
        print(f"В данный момент ваш персонаж находится здесь: X = {x}, Y = {y}")
        break
    
    move_x = input("Введите количество клеток на которое нужно сместиться персонажу по оси X: ")
    move_y = input("Введите количество клеток на которое нужно сместиться персонажу по оси Y: ")

    if is_number(move_x, move_y):
        x += int(move_x)
        y += int(move_y)
        print(f"В данный момент ваш персонаж находится здесь: X = {x}, Y = {y}")

    else:
        print("Invalid argument exception")

    

