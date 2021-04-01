# FIFO data structure
class LinkedListNode:
    def __init__(self,value,nextnode=None):
        self.value=value
        self.nextnode=nextnode

    def TraverseList(self):
        current_node = self
        while True:
            print(current_node.value, "-", end=" ")
            if (current_node.nextnode is None):
                print("None")
                break
            current_node = current_node.nextnode

    def Enqueue(self,value):
        newnode=LinkedListNode(value)
        self.nextnode=newnode
        return self.nextnode


    def Dequeue(self):
        value=self.value
        head=self.nextnode
        return head,value


# driver code
if __name__=="__main__":
    node1=LinkedListNode("Hello ")
    node2=LinkedListNode("Dear ")
    node3=LinkedListNode("Python ")
    node4=LinkedListNode("Programmer")
    head=node1
    tail=node4

    node1.nextnode=node2
    node2.nextnode=node3
    node3.nextnode=node4

    head.TraverseList()
    tail=tail.Enqueue("new word")
    tail=tail.Enqueue(" other node ")
    head.TraverseList()

    head,value=head.Dequeue()
    print(value)
    head,value=head.Dequeue()
    print(value)
    head.TraverseList()






