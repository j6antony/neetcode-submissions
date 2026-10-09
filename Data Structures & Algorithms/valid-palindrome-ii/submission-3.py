class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        if s[0] == s[-1]:
            return self.validPalindrome(s[1:-1])
        else:
            return self.ispalindrome(s[1:]) or self.ispalindrome(s[0:-1])
    def ispalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l+= 1
            r -= 1
        return True
        