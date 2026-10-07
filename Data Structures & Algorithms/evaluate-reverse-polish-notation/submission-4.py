class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst_operator = ["+", "-", "*", "/"]
        stack = []

        for element in tokens:
            if element not in lst_operator:
                stack.append(int(element))
            else:
                second = stack.pop()
                first = stack.pop()
                if element == "+":
                    result = first + second
                    stack.append(result)
                elif element == "-":
                    result = first - second
                    stack.append(result)
                elif element == "*":
                    result = first * second
                    stack.append(result)
                else:
                    result = first / second
                    stack.append(int(result))
        
        return stack[0]