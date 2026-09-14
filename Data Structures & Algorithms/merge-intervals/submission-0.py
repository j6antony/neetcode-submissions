class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort using the first index 
        # the time complexity of the given operation is O(nlogn)
        res = []
        def get_first(interval):
            return interval[0]
        intervals.sort(key=get_first)
        merged = intervals[0]
        i = 0
        while i < len(intervals):
            if merged[1] >= intervals[i][0]:
                merged[0] = min(merged[0], intervals[i][0])
                merged[1] = max(merged[1], intervals[i][1])
            else:
                res.append(merged)
                merged = intervals[i]
            i += 1
        res.append(merged)
        return res
        


