class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str = ""
        p1, p2 = 0, 0
        while p2 < min(len(word2),len(word1)):
            str += word1[p1]
            str += word2[p2]
            p1 += 1
            p2 += 1
        if len(word1) < len(word2):
            str += word2[p2:]
        else:
            str += word1[p1:]
        return str