# task 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        return haystack.find(needle)



if __name__ == '__main__':
    solution = Solution()

    # test case 1
    haystack = "sadbutsad"
    needle = "sad"
    assert solution.strStr(haystack, needle) == 0

    # test case 2
    haystack = "leetcode"
    needle = "leeto"
    assert solution.strStr(haystack, needle) == -1

