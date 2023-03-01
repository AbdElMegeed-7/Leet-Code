# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hash_ = {}
        for n in range(len(nums)):
            if nums[n] in hash_:
                return nums[n]
            hash_[nums[n]] = True


solution = Solution()
print(solution.findDuplicate([1,2,3,4,5,1]))
print(solution.findDuplicate([1,3,4,2,2]))