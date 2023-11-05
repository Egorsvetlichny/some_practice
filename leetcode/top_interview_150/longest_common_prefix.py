# task 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        common_prefix = ""
        min_str = min(strs, key=lambda item: len(item))

        for i in range(len(min_str)):
            sign = min_str[i]
            for j in range(len(strs)):
                if sign != strs[j][i]:
                    return common_prefix
            common_prefix += sign

        return common_prefix


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    strs = ["flower", "flow", "flight"]
    assert solution.longestCommonPrefix(strs) == "fl"

    # test case 2
    strs = ["dog", "racecar", "car"]
    assert solution.longestCommonPrefix(strs) == ""

    # test case 3
    strs = ["ab", "a"]
    assert solution.longestCommonPrefix(strs) == "a"
