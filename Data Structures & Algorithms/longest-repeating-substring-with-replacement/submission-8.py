class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character = {};
        start = 0;
        end = 0;
        count = 0;
        maximum = 0;
        while(end < len(s)):
            character[s[end]] = 1 + character.get(s[end], 0);
            mismatch = end - start + 1 - max(character.values());
            while (mismatch > k):
                character[s[start]] -= 1;
                start +=1;
                mismatch = end - start + 1 - max(character.values());
            count = max(count, end - start + 1);
            end += 1;
        return count;
