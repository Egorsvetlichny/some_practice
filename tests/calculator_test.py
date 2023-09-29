from unittest import TestCase, main
from calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2 + 2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('2 - 2'), 0)

    def test_multi(self):
        self.assertEqual(calculator('2 * 3'), 6)

    def test_devide(self):
        self.assertEqual(calculator('6 / 3'), 2)

    def test_no_signes(self):
        with self.assertRaises(ValueError) as e:
            calculator('abracadabra')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-*/)', e.exception.args[0])

    def test_many_signes(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3*10-1')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.3 + 4.73')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a - b')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])


if __name__ == '__main__':
    main()
