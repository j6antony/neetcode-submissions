class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last = prices[0]
        mins = []
        maxs = []
        ans = 0
        for i in range(len(prices)):
            if last < prices[i]:
                ans += prices[i] - last
            last = prices[i]
        return ans


