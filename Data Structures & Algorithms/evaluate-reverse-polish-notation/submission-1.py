class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        cur = []
        for i in tokens:
            if i == '+':
                num2 = cur.pop()
                num1 = cur.pop()
                cur.append(num1 + num2)
            elif i == '/':
                num2 = cur.pop()
                num1 = cur.pop()
                cur.append(int(num1 / num2))
            elif i == '*':
                num2 = cur.pop()
                num1 = cur.pop()
                cur.append(num1 * num2)
            elif i == '-':
                num2 = cur.pop()
                num1 = cur.pop()
                cur.append(num1 - num2)
            else:
                cur.append(int(i))
        return cur[0]
                
