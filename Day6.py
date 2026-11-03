#_______________Linked List______________
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)

print(n1.data,n1.next)
print(n2.data,n2.next)

#________ Manual Links of nodes_________
head=n1
n1.next=n2
print(n1.data,n1.next)

#________Manual Traversal__________
temp=head
while temp is not None: #while temp !=None
    print(temp.data)
    temp=temp.next

#_________Linked list class creation___________
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def print():
        self.temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

    def insertionAtBegin():
                




myList=Linkedlist()
print(myList)        

