# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next==None:
            return head
        #Reverse the rest of the list not including node
        reverselist_head=self.reverseList(head.next)
        #Use this reversed end of the list and add the current node
        
        # The node after reversed list should the current node
        head.next.next=head
        
        head.next=None
        return reverselist_head
        
    
