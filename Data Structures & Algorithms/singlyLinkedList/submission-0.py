class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.headNode = ListNode(0)
        self.tailNode = self.headNode

    
    def get(self, index: int) -> int:
        curr = self.headNode.next  # Skip dummy head
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # Or raise IndexError

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.headNode.next
        self.headNode.next = newNode
        # If the list was empty, update tail
        if self.tailNode == self.headNode:
            self.tailNode = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        tempNode = self.tailNode
        tempNode.next = newNode
        self.tailNode = newNode
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.headNode

        while i < index and curr.next:
            curr = curr.next
            i += 1
        
        if curr and curr.next:
            if curr.next == self.tailNode:
                self.tailNode = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.headNode.next  # Skip dummy node
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
