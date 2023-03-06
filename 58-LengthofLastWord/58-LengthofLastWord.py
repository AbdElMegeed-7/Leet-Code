class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])
        return len(s.strip().split(" ")[-1])


solution = Solution()
print(solution.lengthOfLastWord("Hello World"))  #  5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # 4
print(solution.lengthOfLastWord("luffy is still joyboy"))  # 6
