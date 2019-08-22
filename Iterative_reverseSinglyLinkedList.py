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
        # Initialize the three pointers
        prev=None
        curr=head
        nextt=None
        
        while(curr!=None):
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        
        return prev