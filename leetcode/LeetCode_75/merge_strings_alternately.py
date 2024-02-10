# task 1768. Merge Strings Alternately

# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        i = 0
        res = []

        while i < len(word1) and i < len(word2):
            res.append(word1[i] + word2[i])
            i += 1

        if i < len(word1):
            res.extend(word1[i::])

        if i < len(word2):
            res.extend(word2[i::])

        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    word1 = "abc"
    word2 = "pqr"
    assert solution.mergeAlternately(word1, word2) == "apbqcr"

    # test case 2
    word1 = "ab"
    word2 = "pqrs"
    assert solution.mergeAlternately(word1, word2) == "apbqrs"

    # test case 3
    word1 = "abcd"
    word2 = "pq"
    assert solution.mergeAlternately(word1, word2) == "apbqcd"
