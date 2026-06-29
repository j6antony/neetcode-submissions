class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set();
        length = 0;
        space = False;
        i = 0;
        j = 0;
        while (i < len(s)):
            if s[i] in found:
                length = max(length, len(found));
                j += 1;
                i = j;
                found = set();
            else:
                found.add(s[i]);
                i += 1;
        length = max(length, len(found));
        return length;




            

                