class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {};
        answer = [];
        for string in strs:
            count = (0,) * 26;
            for char in string:
                count = count[:ord(char) - 97] + (count[ord(char) - 97] + 1,) + count[ord(char) - 97 + 1:];
            try:
                strings[count].append(string);
            except:
                strings[count] = [string];
        for key, value in strings.items():
            answer.append(value);
        return answer;