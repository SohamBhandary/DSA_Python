class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def isEmpty(self):
        return self.start is None
    def insertAtFirst(self,data):
        n=Node(None,data,self.start)
        if not  self.isEmpty():
            self.start.prev=n
        self.start=n
    def insertAtLast(self,data):
        temp=self.start
        if self.start!=None:
            while temp.next!=None:
                temp=temp.next
        n=Node(None,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next       
        return None    
    def insertAfter(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
    def printList(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next


    

