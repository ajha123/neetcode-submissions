class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
       self.head = ListNode(0)
       self.tail = ListNode(0)
       self.head.next = self.tail
       self.tail.prev = self.head
       self.size = 0
        

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.tail and index == 0:
            return cur.val
            
        return -1
        

    def addAtHead(self, val: int) -> None:
        previous = self.head
        next_node = self.head.next
        newNode = ListNode(val)
        newNode.prev = previous
        newNode.next = next_node
        next_node.prev = newNode
        previous.next = newNode
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        previous = self.tail.prev
        next_node = self.tail
        newNode = ListNode(val)
        newNode.next = next_node
        newNode.prev = previous
        previous.next = newNode
        next_node.prev = newNode
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0

        previous = self.head

        for _ in range(index):
            previous = previous.next

        newNode = ListNode(val)
        next_node = previous.next
        newNode.next = next_node
        newNode.prev = previous
        previous.next = newNode
        next_node.prev = newNode
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
            
        cur = self.head.next

        for _ in range(index):
            cur = cur.next

        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)