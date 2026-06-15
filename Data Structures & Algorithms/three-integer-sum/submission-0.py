class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the given list in increasing order
        nums.sort();
        triplets = [];
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue;
            front = i + 1;
            end = len(nums) - 1

            while (front < end):
                sum = nums[i] + nums[front] + nums[end];
                if (sum > 0):
                    end -= 1;
                elif(sum < 0):
                    front += 1;
                else:
                    triplets.append([nums[i], nums[front], nums[end]]);
                    while(front < end and nums[front] == nums[front + 1]):
                        front += 1;
                    while(front < end and nums[end] == nums[end - 1]):
                        end -= 1;
                    #after skipping move the pointers over 1
                    front+=1;
                    end-=1;
           
        return triplets;


