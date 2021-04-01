class LinkedListNode:
    def __init__(self,value=0,parent=None,leftnode=None,rightnode=None):
        self.value=value
        self.parent=parent
        self.left=leftnode
        self.right=rightnode

    def InsertNode(self,value,root=None):
        newnode=LinkedListNode(value)
        if(root is None):
            root=newnode
        else:
            current=root
            parent=None
            while(1):
                parent = current
                if (value < parent.value):
                    current = current.leftnode
                    if (current is None):
                        parent.leftnode = newnode
                else:
                    current = current.rightnode
                    if (current is None):
                        parent.rightnode = newnode

    def PreorderWalk(self, node):
        if (node is not None):
            print(node.value)
            self.PreorderWalk(node.left)
            self.PreorderWalk(node.right)

    def InorderWalk(self,node):
        if(node is not None):
            self.InorderWalk(node.left)
            print(node.value)
            self.InorderWalk(node.right)

    def PostorderWalk(self,node):
        if(node is not None):
            self.PostorderWalk(node.left)
            self.PostorderWalk(node.right)
            print(node.value)

    def TreeSearch(self,node,val):
        if(node is None or val==node.value):
            return node
        else:
            if(val<node.value):
                self.TreeSearch(node.left)
            else:
                self.TreeSearch(node.right)

    def TreeMinimum(self,node):
        tmp=node
        while(tmp.left is not None):
            tmp=tmp.left
        return tmp

    def TreeMaximum(self,node):
        tmp=node
        while(tmp.left is not None):
            tmp=tmp.right
        return tmp

    def TreeSuccessor(self,node):
        if(node.right is not None):
            return self.TreeMinimum(node.right)
        y=node.parent
        while(y is not None and node==y.right):
            node=y
            y=y.parent
        return y

    def TreePredecessor(self,node):
        pass

    def Tree_Insert(self,value):
        tmp=self
        while(tmp is not None):
            tmp_parent=tmp
            if(value<tmp.value):
                tmp=tmp.left
            elif(value>tmp.value):
                tmp=tmp.right
        newnode=LinkedListNode(value)
        tmp=tmp_parent
        newnode.parent=tmp
        if(tmp.left is None and value<tmp.value):
            tmp.left=newnode
        if (tmp.right is None and value > tmp.value):
            tmp.right = newnode


if __name__=="__main__":
    root=LinkedListNode(20)
    root.Tree_Insert(21)
    root.Tree_Insert(30)
    root.Tree_Insert(10)
    root.Tree_Insert(9)
    root.Tree_Insert(15)
    root.Tree_Insert(14)
    root.Tree_Insert(18)
    root.Tree_Insert(25)
    root.Tree_Insert(24)
    root.Tree_Insert(28)
    root.PreorderWalk(root)
    print("=======================")
    root.InorderWalk(root)
    print("=======================")
    root.PostorderWalk(root)



#=======================================================

