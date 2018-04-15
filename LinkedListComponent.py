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
	def numComponents(self, head, G):
		"""
		:type head: ListNode
		:type G: List[int]
		:rtype: int
		"""
		count = 0
		prev = None
		G = set(G)
		while head != None:
			if head.val in G and prev != head:
				count += 1
			if head.next != None:	
				if head.next.val in G:
				    count += 1
				if head.val in G and head.next.val in G:
				    count -= 1
			prev = head.next	
			head = head.next

		return count
		

ll = LinkedList()
ll.add(0)
ll.add(1)
ll.add(3)
ll.add(4)
# 0 -> 1 -> 2
print Solution().numComponents(ll.getHead(), [0, 3, 1, 4])
