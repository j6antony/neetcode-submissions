class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list);
        for i in strs:
            count = [0]*26;
            for j in i:
                count[ord(j) - ord('a')]+=1;
            map[tuple(count)].append(i);
        ans = [];
        for i in map.values():
            ans.append(i);
        return ans;
