class Solution:
    def isPalindrome(self, x: int) -> bool:
        # stack = []
        x = str(x)
        # # for i in x:
        # stack.append(x[::-1])
        if x == x[::-1]:
        # if str(x) == str(x[::-1]):
            return True
        else:
            return False


solution = Solution()
print(solution.isPalindrome(121))
