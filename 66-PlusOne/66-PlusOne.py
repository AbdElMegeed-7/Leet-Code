class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        convert_digits = int(''.join(map(str, digits))) + 1

        # return int dtype
        return [int(digit) for digit in str(convert_digits)]
        # return list(str(convert_digits))  # return str dtype


solution = Solution()
print(solution.plusOne([1, 2, 3]))  # [1,2,4]
print(solution.plusOne([4, 3, 2, 1]))   # [4,3,2,2]
print(solution.plusOne([9]))   # [1,0]
