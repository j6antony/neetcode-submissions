class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = nums.index(min(nums)), nums.index(max(nums))
        def binarysearch(l, r):
            if target < nums[l] or target > nums[r]:
                return False
            while l <= r:
                
                mid = (l + r) // 2
                print (r, l, mid)
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        if r < l:
            if target > nums[r] or target < nums[l]:
                return False
            return binarysearch(0, r) or binarysearch(l, len(nums) - 1)
        
        return binarysearch(l, r)
            
        

            

        