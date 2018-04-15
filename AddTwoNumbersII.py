# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.first = None
		self.last = None

	def add(self, x):
		node = ListNode(x)
		if self.first == None:
			self.first = node
			self.last = node
		else:
			self.last.next = node
			self.last = self.last.next
	
	def getHead(self):
		return self.first	
		
	def cout(self):
		node = self.first
		while node:
			print node.val
			node = node.next
	
	def coutByHead(self, head):
		while head:
			print head.val
			head = head.next
			
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = []
        list2 = []
        
        while l1 != None:
        	list1.append(l1.val)
        	l1 = l1.next
    	
    	while l2 != None:
        	list2.append(l2.val)
        	l2 = l2.next
        
        if len(list1) < len(list2):
        	tmp = list1
        	list1 = list2
        	list2 = tmp
        
        carry, j, result = 0, len(list2) - 1, []
        prev, curr = None, None
        for i in range(len(list1) - 1, -1, -1):
        	s = carry + list1[i] + (list2[j] if j >= 0 else 0)
        	j -= 1
        	if curr == None:
        		prev = ListNode(s % 10)
        		curr = prev
        	else:
        		curr = ListNode(s % 10)
        		curr.next = prev
        		prev = curr
        		
        	carry = s / 10
       	
       	if carry == 1:
       		curr = ListNode(1)
    		curr.next = prev
        return curr
        
l1 = LinkedList()
l1.add(2)

l2 = LinkedList()
l2.add(1)    

l3 = Solution().addTwoNumbers(l1.getHead(), l2.getHead())
while l3 != None:
	print l3.val
	l3 = l3.next 
