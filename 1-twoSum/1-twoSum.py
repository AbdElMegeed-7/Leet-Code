# 1-twoSum #
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for index, number in enumerate(nums):
            # print(index, number)
            if target - number in hash:
                # print(hash[target-number])

                return [hash[target-number], index]
            hash[number] = index


solution = Solution()
print(solution.twoSum([6, 7, 8, 9], 17))
print(solution.twoSum([3,2,4], 6))
