class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode(0, None)
        self.length = 0
        self.tail = self.dummy

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        # traverse the list to find the indexth node
        idx = 0
        cur = self.dummy.next
        while idx != index:
            cur = cur.next
            idx += 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        # add new node before current head
        head = self.dummy.next
        self.dummy.next = ListNode(val, head)

        # update the tail of the list
        while self.tail.next is not None:
            self.tail = self.tail.next

        # update the length of the linked list
        self.length += 1

    def addAtTail(self, val: int) -> None:
        # add new node after the current tail
        self.tail.next = ListNode(val, None)
        self.tail = self.tail.next

        # update the length of the linked list
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 
        
        # traverse the list to find the index - 1 node and add new node
        idx = -1
        cur = self.dummy
        while idx != index - 1:
            cur = cur.next
            idx += 1
        cur.next = ListNode(val, cur.next)

        # update the tail of the list
        while self.tail.next is not None:
            self.tail = self.tail.next

        # update the length of the linked list
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return 
        
        # traverse the list to find the index - 1 node and delete the node after it
        idx = -1
        cur = self.dummy
        while idx != index - 1:
            cur = cur.next
            idx += 1
        before = cur
        after = cur.next.next
        before.next = after

        # update the tail of the list
        while self.tail.next is not None:
            self.tail = self.tail.next
        # need to consider the case where the node removed is the tail
        if index == self.length - 1:
            self.tail = before

        # update the length of the linked list
        self.length -= 1
        

    # Your MyLinkedList object will be instantiated and called as such:
    # obj = MyLinkedList()
    # param_1 = obj.get(index)
    # obj.addAtHead(val)
    # obj.addAtTail(val)
    # obj.addAtIndex(index,val)
    # obj.deleteAtIndex(index)

    '''
    1. get will get the value of the indexth node in the linked list -> maintain length field to easily check if invalid
    2. addAtHead will add a node of value val before the first element of the linked list -> use dummy head to track
    3. addAtTail will add a node of value val as the last element of the linked list -> keep track of the last node
    4. addAtIndex will add a node of value val before the indexth node in the linked list -> O(n) to traverse the list
    5. deleteAtIndex will delete the indexth node in the linked list -> O(n) to traverse the length
    '''