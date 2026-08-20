class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0;
        left, right = 0, 1;
        sub = {};
        maxlen = 1;
        sub[s[0]] = 0;
        while(right < len(s)):
            maxlen = max(len(sub), maxlen)
            if s[right] not in sub:
                sub[s[right]] = right;
                maxlen = max(len(sub), maxlen)    
                right += 1;
            else:
                sub.pop(s[left])
                left += 1;
        return maxlen
    