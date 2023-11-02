# task 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        res = -1
        for symbol in s:
            res = t.find(symbol, res + 1)
            if res == -1:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    s = "abc"
    t = "ahbgdc"
    assert solution.isSubsequence(s, t) == True

    # test case 2
    s = "axc"
    t = "ahbgdc"
    assert solution.isSubsequence(s, t) == False

    # test case 3
    s = "acb"
    t = "ahbgdc"
    assert solution.isSubsequence(s, t) == False

    # test case 4
    s = "b"
    t = "abc"
    assert solution.isSubsequence(s, t) == True