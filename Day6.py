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
n1.next=n2
print(n1.data,n1.next)