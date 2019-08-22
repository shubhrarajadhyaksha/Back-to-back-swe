# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        # Take case of end cases
        if not head :
            return None
        
        #Initialize slow and fast pointers to head node
        
        #pointer which moves one node at a time
        slow=head
        # pointer which moves two nodes at a time
        fast=head
        
        while(fast is not None and fast.next is not None):
            slow=slow.next
            fast=fast.next.next
        
        # when fast pointer reaches the end of linkedlist, slow pointer reaches the middle of linkedlist
        return slow
        
        
        