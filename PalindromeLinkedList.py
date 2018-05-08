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

import math			
class Solution(object):
    def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if head == None: return True

		curr, tail = head, None
		n = 0
		while curr.next != None:
			n += 1
			curr = curr.next

		tail = curr
		n += 1
		mid = n / 2 + 1 if n % 2 != 0 else n / 2
		tail2 = tail
		curr = head
		while curr != tail2:
			if mid > 0:
				mid -= 1
			else:
				tail.next = ListNode(curr.val)
				tail = tail.next

			curr = curr.next
		
		curr = head	
		mid = n / 2
		while mid > 0:
			h = tail2
			t = tail
			while h.next != None and h.next != tail:
				h = h.next
			if h.next != None and curr.next.val != h.next.val:
				return False
			else:
				tail = h
			curr = curr.next
			mid -= 1
		
		if head.val != tail2.val: return False
		
		return True  

ll = LinkedList()
ll.add(1)
ll.add(3)
ll.add(2)
ll.add(4)
ll.add(3)
ll.add(2)
ll.add(1)
print Solution().isPalindrome(ll.getHead())
