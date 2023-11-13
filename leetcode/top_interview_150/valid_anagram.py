# task 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        else:
            s = sorted(s)
            t = sorted(t)
            if s == t:
                return True
            else:
                return False



if __name__ == '__main__':
    solution = Solution()

    # test case 1
    s = "anagram"
    t = "nagaram"
    assert solution.isAnagram(s, t) == True

    # test case 2
    s = "rat"
    t = "car"
    assert solution.isAnagram(s, t) == False