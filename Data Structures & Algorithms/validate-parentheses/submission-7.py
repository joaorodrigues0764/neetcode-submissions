class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if len(s) % 2 != 0:
            return False

        i = 0
        if s[i] == ")" or s[i] == "]" or s[i] == "}":
            return False
        
        while i < len(s):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            
            else:
                if s[i] == ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                    
                elif s[i] == "]":
                    if stack and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                
                elif s[i] == "}":
                    if stack and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False

            i += 1

        return len(stack) == 0 
