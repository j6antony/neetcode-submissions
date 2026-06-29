class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set();
        length = 0;
        j = 0;
        for i in range (len(s)):
            
            while s[i] in found:
                found.remove(s[j]);
                j += 1;
            found.add(s[i]);
            length = max(length, len(found));
        return length;
            





            

                