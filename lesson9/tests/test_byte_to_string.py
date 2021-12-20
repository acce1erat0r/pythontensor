from lesson6_tasks import *
import pytest


@pytest.mark.parametrize("a,expected_result", [([b'\xd1\x82\xd0\xb5\xd1\x81\xd1\x82'], ['тест']),
                                               ([b'\xd1\x81\xd0\xbe\xd0\xbb\xd0\xbd\xd1\x86\xd0\xb5'], ['солнце']),
                                               ([b'12345'], ['12345']),
                                               ([b'tree'], ['tree']),
                                               ([b'L\xd0\x98\xd0\x9dUX'], ['LИНUX'])])
def test_string_to_byte_0(a, expected_result):
    assert Byte_to_string(a) == expected_result

