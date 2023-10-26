# task 58. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        arr_s = s.split()
        return len(arr_s[-1])



if __name__ == '__main__':
    solution = Solution()

    # test case 1
    s = "Hello World"
    assert solution.lengthOfLastWord(s) == 5

    # test case 2
    s = "   fly me   to   the moon  "
    assert solution.lengthOfLastWord(s) == 4

    # test case 3
    s = "luffy is still joyboy"
    assert solution.lengthOfLastWord(s) == 6