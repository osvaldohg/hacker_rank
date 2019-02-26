# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/
# by oz

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    fastpointer=head
    pointer=head
  
    while pointer and fastpointer and fastpointer.next:
        pointer=pointer.next
        fastpointer=fastpointer.next.next
        
        if pointer == fastpointer:
            return 1
        
    return 0
            
    
    
    