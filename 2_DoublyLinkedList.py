class LinkedListNode:
    def __init__(self,value,prevnode=None,nextnode=None):
        self.prevnode=prevnode
        self.value=value
        self.nextnode=nextnode

    def TraverseListForward(self):
        current_node = self
        while True:
            print(current_node.value, "-", end=" ")
            if (current_node.nextnode is None):
                print("None")
                break
            current_node = current_node.nextnode

    def TraverseListBackward(self):
        current_node = self
        while True:
            print(current_node.value, "-", end=" ")
            if (current_node.prevnode is None):
                print("None")
                break
            current_node = current_node.prevnode

# driver code
if __name__=="__main__":
    node1=LinkedListNode("Hello ")
    node2=LinkedListNode("Dear ")
    node3=LinkedListNode(" AI ")
    node4=LinkedListNode("Student")
    head=node1
    tail=node4

    # forward linking
    node1.nextnode=node2
    node2.nextnode=node3
    node3.nextnode=node4

    # backward linking
    node4.prevnode=node3
    node3.prevnode=node2
    node2.prevnode=node1

    head.TraverseListForward()
    tail.TraverseListBackward()







