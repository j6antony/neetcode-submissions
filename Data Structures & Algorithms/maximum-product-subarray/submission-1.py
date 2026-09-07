class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMax, curMin = 1,1
        for n in nums:
            tmp1 = n*curMax
            tmp2 = n*curMin
            curMax  = max(tmp1, tmp2, n)
            curMin = min(tmp1, tmp2, n)
            result = max(result, curMax)
        return result

            