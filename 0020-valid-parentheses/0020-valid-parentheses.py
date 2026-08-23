class Solution(object):
    def isValid(self, s):
        stack = []
        box = {
            ')': '(',
            ']': '[',
            '}': '{'
        }        
        for char in s:            
            if char in box:                
                top_element = stack.pop() if stack else '#'              
                if top_element != box[char]:
                    return False
            else:              
                stack.append(char)      
        return not stack