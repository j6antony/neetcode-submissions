class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {};
        ans = [];
        for i in nums:
            try:
                freq[i] += 1;
            except:
                freq.update({i:1});
        for i in range(k):
            maximum = max(freq, key=freq.get);
            ans.append(maximum);
            del freq[maximum];
        return ans;
            