class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for paren in s:
            if paren in dict:
                if stack and stack[-1]==dict[paren]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paren)
        return not stack


            

         