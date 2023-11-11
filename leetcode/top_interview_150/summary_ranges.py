# task 228. Summary Ranges

# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if not nums:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        else:
            res = []
            a = nums[0]
            b = nums[0]
            for i in range(1, len(nums)):
                if nums[i] - nums[i - 1] == 1:
                    b += 1
                elif a != b:
                    res.append(f'{a}->{b}')
                    a = nums[i]
                    b = nums[i]
                else:
                    res.append(f'{a}')
                    a = nums[i]
                    b = nums[i]

                if nums[i] is nums[-1]:
                    res.append(f'{a}->{b}') if a != b else res.append(f'{a}')

            return res


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    nums = [0, 1, 2, 4, 5, 7]
    assert solution.summaryRanges(nums) == ["0->2", "4->5", "7"]

    # test case 2
    nums = [0, 2, 3, 4, 6, 8, 9]
    assert solution.summaryRanges(nums) == ["0", "2->4", "6", "8->9"]

    # test case 3
    nums = [-1]
    assert solution.summaryRanges(nums) == ["-1"]

    # test case 4
    nums = [1, 2]
    assert solution.summaryRanges(nums) == ["1->2"]

    # test case 5
    nums = []
    assert solution.summaryRanges(nums) == []
