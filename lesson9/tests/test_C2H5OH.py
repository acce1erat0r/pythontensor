import pytest

from lesson6_tasks import *


@pytest.mark.parametrize("a,expected_result", [(['20', '60', '10'], 10),
                                               (['2', '6', '1'], 1),
                                               (['200', '600', '100'], 100),
                                               (['2000', '6000', '1000'], 1000)])
def test_C2HOH(a, expected_result):
    assert C2H5OH(a) == expected_result
