class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        curr = []
        for c in operations:
            if c not in ["+", "D", "C"]:    
                curr.append(int(c))
            if c == "+":
                curr.append(curr[-1]+curr[-2]) 
            if c == "D":
                curr.append(curr[-1]*2) 
            if c == "C":
                curr.pop()  
            
        return sum(curr)