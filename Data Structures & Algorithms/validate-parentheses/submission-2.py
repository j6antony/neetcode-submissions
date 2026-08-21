class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"[":"]", "{":"}", "(":")"};
        stack = [];
        for i in s:
            if i in dic:
                stack.append(i);
            if i in dic.values():
                if len(stack) == 0:
                    return False;
                curent = stack.pop(-1);
                if dic[curent] != i:
                    return False;
        if len(stack) != 0:
            return False;
        return True
