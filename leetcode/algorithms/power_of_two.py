# task 231. Power of Two

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # solution with binary search
        lower = 0
        greater = n

        while lower <= greater:
            middle = (lower + greater) // 2
            if 2 ** middle == n:
                return True
            elif 2 ** middle < n:
                lower = middle + 1
            else:
                greater = middle - 1

        return False

        # solution with recursion
        # if n <= 0:
        #     return False
        # return (n & (n - 1)) == 0


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    n = 1
    assert solution.isPowerOfTwo(n) == True

    # test case 2
    n = 16
    assert solution.isPowerOfTwo(n) == True

    # test case 3
    n = 3
    assert solution.isPowerOfTwo(n) == False

    # test case 4
    n = -8
    assert solution.isPowerOfTwo(n) == False
