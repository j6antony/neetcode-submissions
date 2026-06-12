class Solution:
    def isPalindrome(self, s: str) -> bool:
        string  = "";
        for char in s:
            if (char.isalnum()):
                string += char.lower();
        length = len(string) - 1;
        if (length == -1):
            return True;
        if (length % 2 == 0):
            for index, value in enumerate(string):
                if (index == length/2 and value == string[length-index]):
                    return True;
                if (value != string[length-index]):
                    return False;
        else:
            for index, value in enumerate(string):
                if (index == length//2 and value == string[length-index]):
                    return True;
                if (value != string[length-index]):
                    return False;
    
            