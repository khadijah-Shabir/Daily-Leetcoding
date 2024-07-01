class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for i in s:
            if i in bracket_dict.values():  # Check if i is an opening bracket
                stack.append(i)  # Push opening bracket onto the stack
            elif i in bracket_dict.keys():  # Check if i is a closing bracket
                if not stack or stack.pop() != bracket_dict[i]:
                    return False
            else:
                return False  # If i is neither opening nor closing bracket, return False
        
        return not stack  # Return True if stack is empty, False otherwise


            

         