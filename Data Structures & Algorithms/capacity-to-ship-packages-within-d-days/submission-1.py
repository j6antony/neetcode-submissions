class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            mid = (l + r) // 2

            count = 0
            d =  1
            for i in weights:
                if count + i <= mid:
                    count += i
                else:
                    d += 1
                    count = i
            if d <= days:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        