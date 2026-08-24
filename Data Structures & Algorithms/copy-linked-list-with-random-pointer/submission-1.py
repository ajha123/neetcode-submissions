"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = {}
        current = head

        while current:
            copied_node = Node(current.val)
            old_to_copy[current] = copied_node
            current = current.next
        
        current = head
        while current:
            copy = old_to_copy[current]
            copy.next = old_to_copy.get(current.next)
            copy.random = old_to_copy.get(current.random)
            current = current.next

        return old_to_copy.get(head)
        