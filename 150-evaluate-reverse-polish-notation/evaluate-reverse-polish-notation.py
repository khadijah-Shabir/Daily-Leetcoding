class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                op1 = stack.pop()
                op2 = stack.pop()
                res = op1 + op2
                stack.append(res)
            elif i == "-":
                op1 = stack.pop()
                op2 = stack.pop()
                res = op2 - op1
                stack.append(res)
            elif i == "*":
                op1 = stack.pop()
                op2 = stack.pop()
                res = op1 * op2
                stack.append(res)
            elif i == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                res = int(op2 / op1)
                stack.append(res)
            else:
                stack.append(int(i))

        return stack[0]