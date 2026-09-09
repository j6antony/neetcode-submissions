class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MAX = nums[0]
        cur = 0
        for i in nums:
            if cur < 0:
                cur = 0
            cur += i
            MAX = max(cur, MAX)
        return MAX

        
