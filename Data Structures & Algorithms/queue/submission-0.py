class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.right = Node(0)
        self.left = Node(0)
        self.left.next = self.right
        self.right.prev = self.left


    def isEmpty(self) -> bool:
        return self.left.next == self.right
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        prev_node = self.right.prev
        next_node = self.right
        prev_node.next = new_node
        next_node.prev = new_node
        new_node.prev = prev_node
        new_node.next = next_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)

        prev_node = self.left
        next_node = self.left.next
        prev_node.next = new_node
        next_node.prev = new_node
        new_node.prev= prev_node
        new_node.next = next_node

        

    def pop(self) -> int:
        if self.left.next == self.right:
            return -1
        
        node = self.right.prev
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        return node.val
        

    def popleft(self) -> int:
        if self.left.next == self.right:
            return -1

        node = self.left.next
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        return node.val
        
