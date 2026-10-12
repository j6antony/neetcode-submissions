class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []
        for i in range(len(nums) - 3):
            quad.clear()
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            quad.append(nums[i])
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                quad.append(nums[j])
                l, r = j + 1, len(nums) - 1
                while l < r:
                    total = nums[l] + nums[r] + nums[j] + nums[i]
                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l - 1] == nums[l]:
                            l += 1
                        while l < r and nums[r + 1] == nums[r]:
                            r -= 1
        return res