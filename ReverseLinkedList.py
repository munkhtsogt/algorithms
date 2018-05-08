class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        pre = None
        while head:
        	curr = head
            head = head.next
            curr.next = pre
            pre = curr
        
        return pre
