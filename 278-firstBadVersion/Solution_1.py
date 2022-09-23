# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# 278-firstBadVersion #
class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Base Case
        if n < 2:
            if isBadVersion(n):
                return n
            return -1

        left = 1
        right = n
        while left < right:
            middle = (left + right) // 2

            if isBadVersion(middle) == True:
                right = middle
            else:
                left = middle + 1

        if isBadVersion(right):
            return right
        else:
            return left
