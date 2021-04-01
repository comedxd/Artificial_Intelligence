class LinkedListNode:
    def __init__(self,value,nextnode=None):
        self.value=value
        self.nextnode=nextnode

    def TraverseList(self):
        current_node = self
        while True:
            print(current_node.value, "-", end=" ")
            if (current_node.nextnode is None):
                print("List Ended")
                break
            current_node = current_node.nextnode

# driver code
if __name__=="__main__":
    node1=LinkedListNode("Hello ")
    node2=LinkedListNode("Dear ")
    node3=LinkedListNode("Python ")
    node4=LinkedListNode("Programmer")
    node5 = LinkedListNode("Artificial")
    node6 = LinkedListNode("Intelligence")
    head=node1

    node1.nextnode=node2
    node2.nextnode=node3
    node3.nextnode=node4
    node4.nextnode=node5
    node5.nextnode=node6

    head.TraverseList()







