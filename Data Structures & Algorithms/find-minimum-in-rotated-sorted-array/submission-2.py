class Solution:
    def findMin(self, nums: List[int]) -> int:
        mid = len(nums)//2;
        l, r = 0, len(nums) - 1;
        print(nums);
        if len(nums) == 1:
            return nums[0];
        if len(nums) == 2:
            return min(nums[0], nums[1])
        elif nums[r] > nums[mid]:
            return self.findMin(nums[l:mid + 1]);
        else:
            return self.findMin(nums[mid: r + 1]);

    

