class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^0-9a-zA-Z]', '', s).lower()

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))
