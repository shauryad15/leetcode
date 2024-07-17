class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack:
                    return False
                top = stack.pop()
                if (top == '(' and char == ')') or (top == '[' and char == ']') or (top == '{' and char == '}') :
                    continue 
                else:
                    return False
        return len(stack) == 0