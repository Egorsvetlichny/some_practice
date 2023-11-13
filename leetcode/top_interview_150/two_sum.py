# task 1. Two Sum

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(nums, target) == [0, 1]

    # test case 2
    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [1, 2]

    # test case 3
    nums = [3, 3]
    target = 6
    assert solution.twoSum(nums, target) == [0, 1]
