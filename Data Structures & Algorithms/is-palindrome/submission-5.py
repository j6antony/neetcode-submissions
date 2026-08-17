class Solution:
    def isPalindrome(self, s: str) -> bool:
        #check if it is even length or odd length
        #even length
        new = "";
        start = 0;
        for i in s:
            if i.isalnum():
                new += i;
        new = new.lower();
        end = len(new) - 1;
        print(new);

        if (len(new) % 2 == 0):
            while (start <= len(new)//2 and end >= len(new)//2):
                if (new[start] != new[end]):
                    return False;
                start += 1;
                end -=1;
            return True;
        else:
            while (start <= (len(new) - 1)//2 and end >= (len(new) + 1)//2):
                print(new[start], new[end])
                if (new[start] != new[end]):
                    return False;
                start += 1;
                end -= 1;
            return True;
    
            