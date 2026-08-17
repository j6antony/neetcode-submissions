class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums);
        print(nums);
        count  = 1;
        output = 1;
        first = 0;
        second = 1;
        while (second < len(nums)):
            diff = nums[second] - nums[first];
            if diff == 1:
                count += 1;
            elif diff > 1:
                count = 1;
            output = max(count, output);
            first += 1;
            second += 1;
        if len(nums) == 0: return 0;
        return output;

