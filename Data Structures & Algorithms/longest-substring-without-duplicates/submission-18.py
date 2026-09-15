class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        left, right = 0, 0
        count = 0
        while right < len(s):
            if s[right] not in freq:
                freq[s[right]] = 1
                right += 1
            else:
                freq.pop(s[left])
                left += 1
                if right < left:
                    rigth = left
            count = max(len(freq), count)
        return count

                