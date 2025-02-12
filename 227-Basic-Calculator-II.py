class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(\ \, \\)  # Remove spaces
        stack = []
        num = 0
        prev_op = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  # Build the current number
            
            if char in \+-*/\ or i == len(s) - 1:  # If operator or end of string
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    stack.append(int(stack.pop() / num))  # Truncate toward zero
                
                prev_op = char  # Update operator
                num = 0  # Reset number
        
        return sum(stack)
