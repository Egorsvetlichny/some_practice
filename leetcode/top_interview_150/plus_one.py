# task 66. Plus One

# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits = ''.join(map(lambda x: str(x), digits))
        digits = str(int(digits) + 1)
        digits = ' '.join(digits)

        return list(map(lambda x: int(x), digits.split()))


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    digits = [1, 2, 3]
    assert solution.plusOne(digits) == [1, 2, 4]

    # test case 2
    digits = [4, 3, 2, 1]
    assert solution.plusOne(digits) == [4, 3, 2, 2]

    # test case 3
    digits = [9]
    assert solution.plusOne(digits) == [1, 0]
