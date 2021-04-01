# FIFO value structure
class LinkedListNode:
    def __init__(self,value=0,priority=0,nextnode=None):
        self.value=value
        self.priority=priority
        self.nextnode=nextnode
        self.front=None

    def isEmpty(self):
        return True if self.front == None else False

    def Enqueue(self,value,priority):
        if self.isEmpty() == True:
            self.front = LinkedListNode(value,priority)
            return 1
        else:
            if (self.front.priority < priority):
                newnode = LinkedListNode(value,priority)
                newnode.nextnode = self.front
                self.front = newnode
                return 1
            else:
                temp = self.front
                while temp.nextnode:
                    if priority >= temp.nextnode.priority:
                        break
                    temp = temp.nextnode

                newnode = LinkedListNode(value, priority)
                newnode.nextnode = temp.nextnode
                temp.nextnode = newnode
                return 1

    def Dequeue(self):
        if self.isEmpty() == True:
            return
        else:
            self.front = self.front.nextnode
            return 1

    def GetMax(self):
        if self.isEmpty() == True:
            return
        else:
            return self.front.value

    def Traverse(self):
        if self.isEmpty() == True:
            return "Queue is Empty!"
        else:
            temp = self.front
            while temp:
                print(temp.priority,"-",temp.value, end=" ")
                print()
                temp = temp.nextnode


if __name__ == "__main__":
    pq = LinkedListNode(4,1)
    pq.Enqueue(4, 2)
    pq.Enqueue(5, 1)
    pq.Enqueue(5, 3)
    pq.Enqueue(6, 4)
    pq.Enqueue(7, 0)

    maxpriority_value=pq.GetMax()
    print(maxpriority_value)

    pq.Traverse()
    print("==============================")
    pq.Dequeue()
    pq.Traverse()
