# task 118. Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers.

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        res = []
        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(row)

        return res



if __name__ == '__main__':
    solution = Solution()

    # test case 1
    numRows = 5
    assert solution.generate(numRows) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    # test case 2
    numRows = 1
    assert solution.generate(numRows) == [[1]]
