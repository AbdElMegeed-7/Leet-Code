# 217-containsDuplicate #
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        setNums = set()

        for n in nums:
            if n in setNums:
                return True
            setNums.add(n)
        return False


solution = Solution()

print(solution.containsDuplicate([1, 2, 3, 4, 5]))
print(solution.containsDuplicate([1, 2, 3, 4, 5, 5]))
