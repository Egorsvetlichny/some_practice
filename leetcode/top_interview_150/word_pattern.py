# task 290. Word Pattern

# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match,
# such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        if len(pattern) != len(s.split()):
            return False
        else:
            pattern_s_dict = {}
            s = s.split()
            for i in range(len(s)):
                if pattern[i] in pattern_s_dict and pattern_s_dict[pattern[i]] != s[i]:
                    return False
                elif pattern[i] not in pattern_s_dict and s[i] in pattern_s_dict.values():
                    return False
                pattern_s_dict[pattern[i]] = s[i]

            return True





if __name__ == '__main__':
    solution = Solution()

    # test case 1
    pattern = "abba"
    s = "dog cat cat dog"
    assert solution.wordPattern(pattern, s) == True

    # test case 2
    pattern = "abba"
    s = "dog cat cat fish"
    assert solution.wordPattern(pattern, s) == False

    # test case 3
    pattern = "aaaa"
    s = "dog cat cat dog"
    assert solution.wordPattern(pattern, s) == False

    # test case 4
    pattern = "abba"
    s = "dog dog dog dog"
    assert solution.wordPattern(pattern, s) == False