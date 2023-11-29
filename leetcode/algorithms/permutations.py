# task 46. Permutations

# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.recursion_permute(nums, [], res)
        return res

    def recursion_permute(self, nums, one_permute, result):
        """
        :param nums: List[int]
        :param one_permute: List[int]
        :param result: List[List[int]]
        :return: None
        """
        if len(nums) == len(one_permute):
            result.append(one_permute[:])
            return
        for number in nums:
            if number in one_permute:
                continue
            one_permute.append(number)
            self.recursion_permute(nums, one_permute, result)
            one_permute.pop()


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    nums = [1, 2, 3]
    assert solution.permute(nums) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    # test case 2
    nums = [0, 1]
    assert solution.permute(nums) == [[0, 1], [1, 0]]

    # test case 3
    nums = [1]
    assert solution.permute(nums) == [[1]]
