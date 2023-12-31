# task 88. Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        s = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[s] = nums1[i]
                i -= 1
            else:
                nums1[s] = nums2[j]
                j -= 1

            s -= 1

        # Simple solution:

        # del nums1[m:]
        # nums1 += nums2
        # nums1.sort()

        return nums1


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    assert solution.merge(nums1, m, nums2, n) == [1, 2, 2, 3, 5, 6]

    # test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    assert solution.merge(nums1, m, nums2, n) == [1]

    # test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    assert solution.merge(nums1, m, nums2, n) == [1]
