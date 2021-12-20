# Задание 1.

def String_to_byte(list_string):
    byte_list = []
    for i in list_string:
        byte_list.append(i.encode())

    return byte_list


def Byte_to_string(byte_list):
    list_string = []
    for i in byte_list:
        list_string.append(i.decode())
    return list_string


byte = String_to_byte(['тест', 'солнце', '12345', 'tree', 'LИНUX'])
print(byte[1])
test_string = Byte_to_string(byte)
print(test_string)


# Задание 2.

# Формула молекулы спирта C2H5(OH)
def file_parsing(path):
    with open(path, 'r') as input_data:
        data_elem = input_data.read().split(',')
        return data_elem


def C2H5OH(data):
    elements = data
    C = int(elements[0]) / 2
    H = int(elements[1]) / 6
    O = int(elements[2]) / 1

    spirt = C
    if spirt > H:
        spirt = H

    if spirt > O:
        spirt = O

    with open('files/output.txt', 'w') as output_data:
        output_data.write(str(spirt))

    return spirt


C2H5OH(file_parsing('files/input.txt'))
