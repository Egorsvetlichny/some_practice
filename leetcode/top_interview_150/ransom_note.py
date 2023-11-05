# task 383. Ransom Note

# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        for sign in ransomNote:
            if sign in magazine:
                magazine = magazine.replace(sign, '', 1)
            else:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    ransomNote = "a"
    magazine = "b"
    assert solution.canConstruct(ransomNote, magazine) == False

    # test case 2
    ransomNote = "aa"
    magazine = "ab"
    assert solution.canConstruct(ransomNote, magazine) == False

    # test case 3
    ransomNote = "aa"
    magazine = "aab"
    assert solution.canConstruct(ransomNote, magazine) == True