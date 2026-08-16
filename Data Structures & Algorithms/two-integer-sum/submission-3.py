class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {};
        for i, val in enumerate(nums):
            dif = target - val;
            if dif in map:
                return [map[dif], i];
            else:
                map[val] = i