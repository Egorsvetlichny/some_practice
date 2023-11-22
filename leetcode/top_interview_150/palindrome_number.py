# task 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x = str(x)
        return x == x[::-1]


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    x = 121
    assert solution.isPalindrome(x) == True

    # test case 2
    x = -121
    assert solution.isPalindrome(x) == False

    # test case 3
    x = 10
    assert solution.isPalindrome(x) == False
