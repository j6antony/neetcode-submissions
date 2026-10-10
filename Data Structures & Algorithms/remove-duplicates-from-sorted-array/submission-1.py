class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        last = nums[l]
        unique = 0
        while r <= len(nums):
            if r == len(nums):
                unique += 1
                nums[l] = last
                r += 1
            elif last == nums[r]:
                r += 1
            else:

                unique += 1
                nums[l] = last
                last = nums[r]
                l += 1
                r += 1
        return unique