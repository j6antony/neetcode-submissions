class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their matching opening brackets
        close_to_open = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If it's a closing bracket
            if char in close_to_open:
                # Check if stack is not empty and top of stack matches
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                # If it's an opening bracket, push to stack
                stack.append(char)
        
        # If stack is empty, all brackets were matched correctly
        return len(stack) == 0