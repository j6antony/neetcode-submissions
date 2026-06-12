class Solution:
    #find the lowest number in the set
    def lowest(self, nums: Set[int]) -> int:
        lowest = min(nums)
        return lowest;
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums);
        length = 0;
        while (len(n) != 0):
            low = self.lowest(n);
            index = 0;
            while ((low + index) in n):
                n.discard(low+index);
                index += 1;
            if(index > length):
                length = index;
        return length;
                
            
    
    
    
            