class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "";
        for s in strs:
            length = len(s);
            encoded += f"{length}#{s}"
        return encoded;

    def decode(self, s: str) -> List[str]:
        length = "";
        strs = [];
        index = 0;
        while(index < len(s)):
            if (s[index] != "#"):
                length += s[index];
                index+= 1;
                continue;
            strs.append(s[index+1:index + 1 + int(length)]);
            index += 1+int(length);
            length = "";
        return strs;

            

