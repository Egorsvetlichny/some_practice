# task 172. Factorial Trailing Zeroes

# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 5:
            return 0
        else:
            factorial_n = 1
            for i in range(2, n + 1):
                factorial_n *= i

        factorial_n = str(factorial_n)[::-1]
        zero_trailing_counter = 0

        for digit in factorial_n:
            if digit == '0':
                zero_trailing_counter += 1
            else:
                return zero_trailing_counter


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    n = 3
    assert solution.trailingZeroes(n) == 0

    # test case 2
    n = 5
    assert solution.trailingZeroes(n) == 1

    # test case 3
    n = 0
    assert solution.trailingZeroes(n) == 0

    # test case 4
    n = 7
    assert solution.trailingZeroes(n) == 1
