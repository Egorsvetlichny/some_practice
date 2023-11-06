# task 151. Reverse Words in a String

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.split()
        s.reverse()
        return ' '.join(s)



if __name__ == '__main__':
    solution = Solution()

    # test case 1
    s = "the sky is blue"
    assert solution.reverseWords(s) == "blue is sky the"

    # test case 2
    s = "  hello world  "
    assert solution.reverseWords(s) == "world hello"

    # test case 3
    s = "a good   example"
    assert solution.reverseWords(s) == "example good a"