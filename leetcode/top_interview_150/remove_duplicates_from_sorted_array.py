# task 26. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order.
# Remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# 1) Change the array nums such
# that the first k elements of nums contain the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# 2) Return k.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # dupl = nums[0] - 1
        # i = 0
        # while i != len(nums):
        #     if nums[i] == dupl:
        #         nums.remove(dupl)
        #     else:
        #         dupl = nums[i]
        #         i += 1

        nums = list(set(nums))
        nums.sort()

        return len(nums)


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert solution.removeDuplicates(nums) == 5

    # test case 2
    nums = [1, 1, 2]
    assert solution.removeDuplicates(nums) == 2
