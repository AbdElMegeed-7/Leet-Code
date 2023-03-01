# Time complexity: O(nlogn)
# Space complexity: O(1) if you are allowed to modify the input, O(n) else
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        for n in range(len(nums)):
            if nums[n] == nums[n + 1]:
                return nums[n]


solution = Solution()
print(solution.findDuplicate([1, 2, 3, 4, 5, 1]))
print(solution.findDuplicate([1, 3, 4, 2, 2]))
print(solution.findDuplicate([3, 1, 3, 4, 2]))
