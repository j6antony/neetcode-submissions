class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {};
        for i, n in enumerate(nums):
            indices[n] = i;

        for index, num in enumerate(nums):
            newtarget = target - num;
            if newtarget in indices and indices[newtarget] != index:
                return [index, indices[newtarget]];
