class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        if self.start==None:
            return True
        else:
            return False
        
    def insertAtFirst(self,data):
        n=Node(data,self.start)
        self.start=n

    def insertAtLast(self,data):
        n=Node(data)
        if not self.isEmpty():
            temp=self.start
            while(temp.next is not None):
                temp=temp.next
            temp.next=n
        else :
            self.start=n
    def search(self,data):
        temp=self.start
        while(temp is not None):
            if temp.item==data:
                return temp
            else:
                temp=temp.next
        return None
    def insertAfter(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def printList(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next

    def deleteFirst(self):
        if self.start is not None:
            self.start=self.start.next
    def deleteLast(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else :
            temp=self.start
            while(temp.next.next is not None):
                temp=temp.next
            temp.next=None
    def deleteItem(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
                          

       

            

        

myList=SLL()
myList.insertAtFirst(20)
myList.insertAtLast(30)
myList.insertAfter(myList.search(20),25)
myList.deleteItem(25)


myList.printList()


       


        
