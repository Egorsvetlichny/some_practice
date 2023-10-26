# task 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        common_substring = ""
        for i in range(len(strs[0])):
            symbol = strs[0][i]

            for j in range(1, len(strs)):
                if strs[j][i] != symbol or len(strs[j]) < i:
                    return common_substring
            common_substring += symbol

        return common_substring


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    strs = ["flower", "flow", "flight"]
    assert solution.longestCommonPrefix(strs) == "fl"

    # test case 2
    strs = ["dog", "racecar", "car"]
    assert solution.longestCommonPrefix(strs) == ""
