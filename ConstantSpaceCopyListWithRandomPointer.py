"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        cur=head
        while cur!=None:
            nex=cur.next
            node=Node(cur.val,None,None)
            cur.next=node
            node.next=nex
            cur=nex
        cur=head
        
        while cur!=None:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next
            
        dummyhead=Node(0,None,None)
        cur2=dummyhead
        cur=head
        
        while cur!=None:
            nex=cur.next.next
            cur2.next=cur.next
            cur2.next.next=None
            cur2=cur2.next
            cur.next=nex
            cur=nex
            
        return dummyhead.next
            
            
            
        