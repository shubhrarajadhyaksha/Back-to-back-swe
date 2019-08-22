"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        hashmap={}
        
        cur=head
        
        while(cur!=None):
            n=Node(cur.val,None,None)
            hashmap[cur]=n
            cur=cur.next
        cur=head
        while(cur!=None):
            if cur.next:
                hashmap[cur].next=hashmap[cur.next]
            
            if cur.random:
                hashmap[cur].random=hashmap[cur.random]
            cur=cur.next
        
        return hashmap[head]
            
            
            
        
        
        