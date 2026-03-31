class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        my_stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                num2 = int(my_stack.pop())
                num1 = int(my_stack.pop())

                if i == "+":
                    my_stack.append(num1 + num2)
                elif i == "-":
                    my_stack.append(num1 - num2)
                elif i == "*":
                    my_stack.append(num1 * num2)
                elif i == "/":
                    my_stack.append(int(num1 / num2))
            else:
                my_stack.append(int(i))
            
        return my_stack[0]
                