class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: 
            return int(tokens[-1])
            
        operators = {'+', '-', '*', '/'}
        stack = []
        curr_eval = 0

        for token in tokens: 
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "-":
                op1, op2 = int(stack.pop()), int(stack.pop())
                stack.append(op2 - op1)
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == "/":
                op1, op2 = int(stack.pop()), float(stack.pop())
                stack.append(int(op2 / op1))
        
            else:             
                stack.append(token)

        return int(stack[-1])
