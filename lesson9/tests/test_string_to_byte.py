from lesson6_tasks import *
import pytest


@pytest.mark.parametrize("a,expected_result", [(['test'], [b'test']),
                                               (['привет'], [b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82']),
                                               (['summer*!'], [b'summer*!'])])
def test_string_to_byte_0(a, expected_result):
    assert String_to_byte(a) == expected_result

