class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        minimum = float('inf')
        for r in range (len(nums)):
            sum += nums[r]
            while sum >= target:
                minimum = min(minimum, r - l + 1)
                sum -= nums[l]
                l += 1
        if minimum == float('inf'):
            return 0
        return minimum


        