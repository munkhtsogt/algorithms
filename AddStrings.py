class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
        	tmp = num1
        	num1 = num2
        	num2 = tmp
    	
    	carry, j = 0, len(num2) - 1
    	result = ""
    	for i in range(len(num1) - 1, -1, -1):
    		a = ord(num1[i]) - 48
    		b = ord(num2[j]) - 48 if j >= 0 else 0
    		r = carry + a + b
    		carry = r / 10
    		result = str(r % 10) + result
        	j -= 1
        	
        if carry == 1:
        	result = str(carry) + result
        
        return result
        
print Solution().addStrings("555", "555")
