class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return nums
        pivot = nums[len(nums)//2]
        less, greater, same = [], [], []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                same.append(num)
        return self.sortArray(less) + same + self.sortArray(greater)