class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1;
        mprofit = 0;
        while (right < len(prices)):
            profit = prices[right] - prices[left];
            if profit > 0:
                mprofit = max(profit, mprofit);
            if prices[right] < prices[left]:
                left = right;
            right += 1;

            
        return mprofit;
            