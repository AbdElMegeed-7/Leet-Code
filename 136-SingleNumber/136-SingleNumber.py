class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        stack = []
        for n in nums:
            if n in stack:
                stack.remove(n)
            # print(stack)
            else:
                stack.append(n)

        return stack[0]


solution = Solution()
print(solution.singleNumber(([2, 2, 1])))
print(solution.singleNumber([2, 3, 4, 4, 3]))
print(solution.singleNumber([4, 1, 2, 1, 2]))
