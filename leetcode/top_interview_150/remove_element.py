# task 27. Remove Element

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# 1) Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# 2) Return k.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while val in nums:
            nums.remove(val)

        return len(nums)


if __name__ == '__main__':
    # test case
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2

    solution = Solution()
    assert solution.removeElement(nums, val) == 5
