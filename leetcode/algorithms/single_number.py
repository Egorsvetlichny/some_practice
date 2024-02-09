# task 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        repeat_counter = {}
        for item in nums:
            if repeat_counter.get(item, 0):
                repeat_counter[item] += 1
            else:
                repeat_counter[item] = 1

        for item in repeat_counter:
            if repeat_counter[item] == 1:
                return item


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    nums = [2, 2, 1]
    assert solution.singleNumber(nums) == 1

    # test case 2
    nums = [4, 1, 2, 1, 2]
    assert solution.singleNumber(nums) == 4

    # test case 3
    nums = [1]
    assert solution.singleNumber(nums) == 1
