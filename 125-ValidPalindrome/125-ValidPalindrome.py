class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^0-9a-zA-Z]', '', s).lower()
        return s == s[::-1]


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))
