# task 50. Pow(x, n)

# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        else:
            if n < 0:
                x = 1 / x
                n *= -1
            x_powed = 1
            while n:
                if n % 2 == 1:
                    x_powed *= x
                x *= x
                n = n // 2

            return round(x_powed, 5)


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    x = 2.00000
    n = 10
    assert solution.myPow(x, n) == 1024.00000

    # test case 2
    x = 2.10000
    n = 3
    assert solution.myPow(x, n) == 9.26100

    # test case 3
    x = 2.00000
    n = -2
    assert solution.myPow(x, n) == 0.25000
