# task 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = [[]]
        for item in strs:
            if not res[0]:
                res[0].append(item)
            else:
                for list in res:
                    if len(item) == len(list[0]) and sorted(item) == sorted(list[0]):
                        list.append(item)
                        break
                else:
                    res.append([item])
        return res


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert solution.groupAnagrams(strs) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    # test case 2
    strs = [""]
    assert solution.groupAnagrams(strs) == [[""]]

    # test case 3
    strs = ["a"]
    assert solution.groupAnagrams(strs) == [["a"]]
