class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        i = 0
        for p in range(len(prices)):
            if prices[p] < prices[i]:
                i = p
            max_profit = max(max_profit, prices[p] - prices[i])
        return max_profit

        """
        def maxProfit(self, prices: List[int]) -> int:
            max_profit = 0
            min_buy = float('inf')
            for price in prices:
                min_buy=min(min_buy, price)
                max_profit=max(max_profit, price-min_buy)
            return max_profit
        """


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
