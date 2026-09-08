class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: 
        #remove the duplicates as it is irrelevent
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for n in range(i + 1, len(nums)):
                if nums[i] < nums[n]:
                    dp[i] = max(dp[i], 1 + dp[n])
 
        return max(dp)


