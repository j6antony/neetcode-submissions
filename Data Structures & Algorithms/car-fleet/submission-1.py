class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new = []
        #write as tuples
        for i in range(len(position)):
           new.append((position[i], speed[i])) 
        new.sort(key=lambda x: x[0], reverse=True)
        times = {}
        max = -1
        for i in new:
            x = (target - i[0])/i[1]
            if max == -1:
                times[x] = 1
                max = x
                continue
            elif max > x:
                continue
            elif max < x:
                max = x
            times[x] = 1 + times.get(x, 0)
        return len(times)

            
 
    