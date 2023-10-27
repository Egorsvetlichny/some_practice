# task 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = ''.join(symbol.lower() for symbol in s if symbol.isalnum())

        return s == s[::-1]


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    s = "A man, a plan, a canal: Panama"
    assert solution.isPalindrome(s) == True

    # test case 2
    s = "race a car"
    assert solution.isPalindrome(s) == False

    # test case 3
    s = " "
    assert solution.isPalindrome(s) == True
