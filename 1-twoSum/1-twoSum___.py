class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_ = {}
        for n in nums:
            if hash_.get(target - n):
                return True
            else:
                hash_[n] = n
        return False


solution = Solution()
print(solution.twoSum([6, 7, 8, 9], 17))
print(solution.twoSum([3, 2, 4], 8))
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
