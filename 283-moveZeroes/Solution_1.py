class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                zero = nums[i]
                nums.remove(nums[i])
                nums.append(zero)
        return nums


solution = Solution()

print(solution.moveZeroes([0, 1, 2, 3, 0, 4, 5]))
