
x = 0
y = 0


move_x = input("Введите количество клеток на которое нужно сместиться персонажу по оси X: ")
move_y = input("Введите количество клеток на которое нужно сместиться персонажу по оси Y: ")


def is_number(x, y):
    try:
            int(x)
            int(y)
            return True
    except ValueError:
            return False


if is_number(move_x, move_y):
    x += int(move_x)
    y += int(move_y)
else:
    print("Invalid argument exception")


print(f"В данный момент ваш персонаж находится здесь: X = {x}, Y = {y}")

