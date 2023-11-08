# task 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        else:
            charlist_s = {}
            charlist_t = {}

            for i in range(len(s)):
                if s[i] in charlist_s and charlist_s[s[i]] != t[i]:
                    return False
                elif t[i] in charlist_t and charlist_t[t[i]] != s[i]:
                    return False
                else:
                    charlist_s[s[i]] = t[i]
                    charlist_t[t[i]] = s[i]

            return True


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    s = "egg"
    t = "add"
    assert solution.isIsomorphic(s, t) == True

    # test case 2
    s = "foo"
    t = "bar"
    assert solution.isIsomorphic(s, t) == False

    # test case 3
    s = "paper"
    t = "title"
    assert solution.isIsomorphic(s, t) == True
