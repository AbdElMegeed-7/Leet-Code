class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] < target:
                left += 1
            elif nums[right] + nums[right] > target:
                right -= 1
        return []


solution = Solution()
print(solution.twoSum([6, 7, 8, 9], 17))
print(solution.twoSum([3, 2, 4], 8))
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
