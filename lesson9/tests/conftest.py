import pytest


@pytest.fixture(autouse=True)
def clean_text_file():
    with open("tests/testfile_input.txt", 'w'):
        pass
