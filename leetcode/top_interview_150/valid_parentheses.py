# task 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        signs_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for sign in s:
            if sign in signs_dict.values():
                stack.append(sign)
            elif len(stack) == 0 or sign not in signs_dict.keys() or signs_dict[sign] != stack.pop():
                return False
        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()

    # test case 1
    s = "()"
    assert solution.isValid(s) == True

    # test case 2
    s = "(]"
    assert solution.isValid(s) == False

    # test case 3
    s = "()[]{}"
    assert solution.isValid(s) == True

    # test case 4
    s = "{[]}"
    assert solution.isValid(s) == True
