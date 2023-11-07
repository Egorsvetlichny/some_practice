# task 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        sum = 0
        res = float('inf')
        left = 0

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                res = min(res, right - left + 1)
                sum -= nums[left]
                left += 1

        return 0 if res == float('inf') else res


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    assert solution.minSubArrayLen(target, nums) == 2

    # test case 2
    target = 4
    nums = [1, 4, 4]
    assert solution.minSubArrayLen(target, nums) == 1

    # test case 3
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    assert solution.minSubArrayLen(target, nums) == 0
