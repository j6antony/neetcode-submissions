class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = {};
        sub = {};
        for i in s1:
            s1map[i] = 1 + s1map.get(i, 0);
        start = 0;
        end = len(s1) - 1;
        while (end < len(s2)):
            origin = start;
            while (origin <= end):
                sub[s2[origin]] = 1 + sub.get(s2[origin], 0);
                origin += 1;
            if sub == s1map:
                return True;
            sub = {};
            end += 1;
            start +=1;
        return False;
