# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hash_ = {}
        for element in nums:
            if hash_.get(element):
                return element
            else:
                hash_[element] = True

solution = Solution()
print(solution.findDuplicate([1,2,3,4,5,1]))
print(solution.findDuplicate([1,3,4,2,2]))
print(solution.findDuplicate([3,1,3,4,2]))