class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        i = 0

        while i < len(temperatures):
            if len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                    previous = stack.pop()
                    result[previous] = i - previous
                stack.append(i)
            
            else:
                stack.append(i)
            
            i += 1
        
        return result

