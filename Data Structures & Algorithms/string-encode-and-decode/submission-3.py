class Solution:

    def encode(self, strs: List[str]) -> str:
        output = "";
        for i in strs:
            if (len(i) == 0):
                output += "03";
            else:
                output += "#3";
                output += i;
                output += "#3";
        return output;
    def decode(self, s: str) -> List[str]:
        ans = [];
        word = "";
        first = 0;
        second = 1;
        while (first < len(s)):
            if (second < len(s) and s[first] == "#" and s[second] == "3"):
                first += 2;
                second += 2;
                if (len(word) != 0):
                    ans.append(word);
                word = "";
            elif (second < len(s) and s[first] == "0" and s[second] == "3"):
                ans.append("");
                first += 2;
                second += 2;
            else:
                word += s[first];
                first += 1;
                second += 1;
        return ans;