class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in range (len(s)):
            try:
                s_dict[s[i]] += 1
            except:
                s_dict[s[i]] = 1

        for i in range (len(t)):
            try:
                t_dict[t[i]] += 1
            except:
                t_dict[t[i]] = 1

        if (len(s_dict) != len(t_dict)):
            return False

        for key, value in s_dict.items():
            try:
                if t_dict[key] != value :
                    return False
            except:
                return False
        return True