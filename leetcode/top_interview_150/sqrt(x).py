# task 69. Sqrt(x)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        low = 0
        high = x

        while low <= high:
            middle = (low + high) // 2
            sqr = middle * middle
            if sqr == x:
                return middle
            elif sqr < x:
                low = middle + 1
            elif sqr > x:
                high = middle - 1

        return high


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    x = 4
    assert solution.mySqrt(x) == 2

    # test case 2
    x = 8
    assert solution.mySqrt(x) == 2

    # test case 2
    x = 0
    assert solution.mySqrt(x) == 0