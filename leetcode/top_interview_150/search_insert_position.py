# task 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low = 0
        high = len(nums) - 1

        while low <= high:
            middle_index = (low + high) // 2
            if target == nums[middle_index]:
                return middle_index
            elif target < nums[middle_index]:
                high = middle_index - 1
            elif target > nums[middle_index]:
                low = middle_index + 1

        return low



if __name__ == '__main__':
    solution = Solution()

    # test case 1
    nums = [1, 3, 5, 6]
    target = 5
    assert solution.searchInsert(nums, target) == 2

    # test case 2
    nums = [1, 3, 5, 6]
    target = 2
    assert solution.searchInsert(nums, target) == 1

    # test case 3
    nums = [1, 3, 5, 6]
    target = 7
    assert solution.searchInsert(nums, target) == 4

    # test case 4
    nums = [1, 3, 5, 6]
    target = 0
    assert solution.searchInsert(nums, target) == 0
