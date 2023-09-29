import pytest

from calculator import calculator


def test_plus():
    assert calculator('2 + 3') == 5


def test_minus():
    assert calculator('2 - 1') == 1


def test_multi():
    assert calculator('2 * 3') == 6


def test_devide():
    assert calculator('2 / 2') == 1


def test_no_signes():
    with pytest.raises(ValueError) as error:
        calculator('abra-cadabra')
    assert 'Выражение должно содержать 2 целых числа и 1 знак' == error.value.args[0]


def test_many_signes():
    with pytest.raises(ValueError) as error:
        calculator('2+3*10-1')
    assert 'Выражение должно содержать 2 целых числа и 1 знак' == error.value.args[0]


def test_no_ints():
    with pytest.raises(ValueError) as error:
        calculator('2.3 + 4.73')
    assert 'Выражение должно содержать 2 целых числа и 1 знак' == error.value.args[0]

def test_strings():
    with pytest.raises(ValueError) as error:
        calculator('a - b')
    assert 'Выражение должно содержать 2 целых числа и 1 знак' == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
