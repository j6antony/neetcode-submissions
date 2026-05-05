class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            newtarget = target - num;
            newnums = nums.copy();
            newnums.pop(index);
            if(newtarget in newnums):
                return [index, newnums.index(newtarget) + 1]
