class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start is None

    def insertAtFirst(self, data):
        n = Node(None, data, self.start)
        if not self.isEmpty():
            self.start.prev = n
        self.start = n

    def insertAtLast(self, data):
        n = Node(None, data, None)
        if self.isEmpty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            n.prev = temp

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insertAfter(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def printList(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, data):
        if self.start is None:
            return
        temp = self.start
        if temp.item == data:  # Deleting the first item
            self.start = temp.next
            if self.start:
                self.start.prev = None
            return
        while temp is not None:
            if temp.item == data:
                if temp.next is not None:
                    temp.next.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = temp.next
                return
            temp = temp.next

# Test the DLL
myList = DLL()
myList.insertAtFirst(10)
myList.insertAtLast(20)
myList.insertAfter(myList.search(10), 15)
myList.printList()  # Output: 10 15 20
myList.delete_first()
myList.printList()  # Output: 15 20
