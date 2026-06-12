class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nonzero = 1;
        zeros = 0;
        ans = []
        for i in nums:
            if(i == 0):
                zeros += 1;
            else:
                nonzero *= i;
        if (zeros >= 2):
            return [0] * len(nums);
        elif (zeros == 1):
            for i in nums:
                if (i != 0):
                    ans.append(0);
                else:
                    ans.append(nonzero);
            return ans;
        else:
            for i in nums:
                ans.append(int(nonzero/i));
            return ans
                
        