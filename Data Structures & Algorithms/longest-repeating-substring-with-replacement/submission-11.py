class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curent  = k;
        left, right = 0, 0;
        maxlen = max(1, k);
        freq = {};
        maximum  = [0,0]
        length = 0;
        missing = 0;
        for right in range(len(s)):

            freq[s[right]] = freq.get(s[right], 0) + 1;
            length = right - left + 1;
            frequent = max(freq.values())
            missing  = length - frequent;
            if missing > k:
                freq[s[left]] -= 1;
                left += 1
            maxlen = max(right - left + 1, maxlen);
   
        return maxlen
    
           





            

            


