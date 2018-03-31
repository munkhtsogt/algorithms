class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        st = []
        for op in ops:
        	if op.lstrip("-").isdigit():
        		st.append(int(op))
        	elif op == "C":
        		st.pop()
        	elif op == "D":
        		st.append(st[-1] * 2)
        	else:
        		st.append(st[-1] + st[-2])
        		
       	return sum(st)
        
        
sol = Solution()
ops = ["5","-2","4","C","D","9","+","+"]
print sol.calPoints(ops)
