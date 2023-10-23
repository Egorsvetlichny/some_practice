# task 169. Majority Element

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        majority_dict = {}
        for element in nums:
            if element in majority_dict:
                majority_dict[element] += 1
            else:
                majority_dict[element] = 1

        count_majority_val = max(majority_dict.values())
        majority_val = [key for key in majority_dict if majority_dict[key] == count_majority_val]
        return majority_val[0]


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    nums1 = [3, 2, 3]
    assert solution.majorityElement(nums1) == 3

    # test case 2
    nums1 = [2, 2, 1, 1, 1, 2, 2]
    assert solution.majorityElement(nums1) == 2
