class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0;
        for i in nums:
            if i == 0:
                zeros += 1;
        ans = [];
        if zeros == 0:
            total = 1;
            for i in nums:
                total *= i;
            for i in nums:
                ans.append(total//i);
        elif zeros > 1:
            for i in nums:
                ans.append(0);
            return ans;
        else:
            index = 0;
            multiple = 1;
            for value, i in enumerate(nums):
                if i != 0:
                    multiple *= i;
                    ans.append(0);
                else:
                    ans.append(0);
                    index = value;
            ans[index] = multiple;
        
        return ans;

