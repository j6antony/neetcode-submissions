class Solution:
    def rob(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        for i in nums:
            temp = max(i + max1, max2)
            max1 = max2
            max2 = temp

        return max2