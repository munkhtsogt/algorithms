class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        five = ten = 0
        for bill in bills:
            if bill == 5: five += 1
            elif bill == 10:
                if not five: return False 
                five -= 1
                ten += 1
            elif bill == 20:
                if ten and five:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
            
            if five < 0: return False

        return True

sol = Solution()
print sol.lemonadeChange([5,5,5,10,20])
print sol.lemonadeChange([5,5,10])
print sol.lemonadeChange([5,5,10,10,20])
print sol.lemonadeChange([10, 10])
print sol.lemonadeChange([5,5,5,5,20,20,5,5,20,5])
print sol.lemonadeChange([])