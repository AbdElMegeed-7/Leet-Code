class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        for n in range(len(nums)):
            for i in range(n + 1, len(nums)):
                if nums[n] == nums[i]:
                    return nums[n]
        

solution = Solution()
print(solution.findDuplicate([1,2,3,4,5,1]))
print(solution.findDuplicate([1,3,4,2,2]))
print(solution.findDuplicate([3,1,3,4,2]))