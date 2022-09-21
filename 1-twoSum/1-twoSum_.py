# Time complexity: O(n�)
# Space complexity: O(1)
# Too Slow
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for n in range(len(nums)):
            for i in range(n + 1, len(nums)):
                if nums[n] + nums[i] == target:
                    return [n, i]
        return []


solution = Solution()
print(solution.twoSum([6, 7, 8, 9], 17))
print(solution.twoSum([3, 2, 4], 8))
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3,2,4], 6))
