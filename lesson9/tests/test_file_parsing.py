from lesson6_tasks import *


def test_file_parsing():
    test_data = ['9', '22', '13']
    with open("tests/testfile_input.txt", 'a') as f_o:
        f_o.write(','.join(test_data))
    assert test_data == file_parsing('tests/testfile_input.txt')
