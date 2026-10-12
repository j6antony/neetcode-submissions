import math
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        sum = 0
        while l <= r:
            sum = people[l] + people[r]
            if l == r:
                boats += 1 
                l += 1
                r -= 1           
            elif sum > limit:
                boats += 1
                r -= 1
            elif sum <= limit:
                boats += 1
                l += 1
                r -= 1
            sum = 0
        
        return boats