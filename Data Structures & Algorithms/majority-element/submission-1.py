class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2
        dic = {}
        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
        return max(dic, key=dic.get)
