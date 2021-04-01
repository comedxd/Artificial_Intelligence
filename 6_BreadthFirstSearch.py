class LinkedListNode:
    def __init__(self,value=0,parent=None,leftnode=None,rightnode=None):
        self.value=value
        self.parent=parent
        self.left=leftnode
        self.right=rightnode
        self.visited=False

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

    def Breadth_First_Traversal(self,  Graph, root):
        """
        create a queue Q
        mark v as visited and put v into Q
        while Q is non-empty
            remove the head u of Q
            mark and enqueue all (unvisited) neighbors of u
        """
        visited = []  # List to keep track of visited nodes.
        queue = []  # Initialize a queue
        visited.append(root)
        queue.append(root)
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    def Breadth_First_Traversal_Tree(self, root):
        #visited = []    # List to keep track of visited nodes.
        queue = []      # Initialize a queue
        #visited.append(root)
        queue.append(root)
        while queue:
            s = queue.pop(0)
            print(s.value, end=" ")
            for child in (s.left,s.right):
                if (child is not None ) and (child.visited==False):
                    child.visited=True
                    queue.append(child)

    def Breadth_First_Traversal_Tree_Search(self, root,value):
        queue = []
        values=[]
        queue.append(root)
        values.append(root.value)
        while queue:
            s = queue.pop(0)
            #print(s.value, end=" ")
            if(s.value==value):
                print("Value found")
                return
            print(values)
            values.clear()
            for child in (s.left,s.right):
                if (child is not None ) and (child.visited==False):
                    child.visited=True
                    queue.append(child)
                    values.append(child.value)



if __name__=="__main__":
    # Assignment-1: implement the BFT using tree data structure
    # Assignment-2: convert the bft search method to Breadth First Search where user passes a value and
    # using breadth first search, find the value
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    tree=LinkedListNode()
    tree.Breadth_First_Traversal(graph,'A')

    #=========== using tree data structure
    root = LinkedListNode(20)
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
    #root.Breadth_First_Traversal_Tree(root)
    print("===============================")
    root.Breadth_First_Traversal_Tree_Search(root, 24)



