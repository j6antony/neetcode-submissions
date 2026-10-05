class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
        thresh = len(nums) // 3
        print(dic)
        ans = []
        for key, value in dic.items():
            if thresh < value:
                ans.append(key)
        return ans