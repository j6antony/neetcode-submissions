class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = {"one": 0, "two": 0, "zero": 0}
        for num in nums:
            if num == 0:
                dic["zero"] += 1
            elif num == 1:
                dic["one"] += 1
            else:
                dic["two"] += 1
        cur = "zero"
        zero = dic["zero"] - 1
        one = dic["one"] + dic["zero"] - 1
        two = dic["one"] + dic["two"] + dic["zero"] - 1
        for i in range(len(nums)):
            if i <= zero:
                nums[i] = 0
            elif i <= one:
                nums[i] = 1
            else:
                nums[i] = 2
