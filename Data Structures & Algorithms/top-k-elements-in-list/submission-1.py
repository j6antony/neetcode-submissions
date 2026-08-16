class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = defaultdict(list);
        for i in nums:
            freq[i] = freq.get(i, 0) + 1;
        for i in freq:
            bucket[freq[i]].append(i);

        pointer = len(nums);
        ans = [];
        while (k > 0):
            res = bucket[pointer];
            if len(res) == 0:
                pointer -= 1;
                continue;
            ans.append(res[0]);
            k -= 1;
            bucket[pointer].pop(0);
        return ans;
    

        