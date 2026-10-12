class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            elif r - l < k:
                r += 1
            else:
                l += 1
                r = l + 1
        return False
