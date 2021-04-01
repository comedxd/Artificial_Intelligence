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


    def Depth_First_Traversal_List(self,visited,graph,node):
        """
        DFS(G, u)
        u.visited = true
        for each v ∈ G.Adj[u]
            if v.visited == false
            DFS(G,v)
        """
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                    self.Depth_First_Traversal_List(visited, graph, neighbour)

    def Depth_First_Traversal_Tree(self,root):
        if root is None:
            return
        else:
            print(root.value, end=" ")
            self.Depth_First_Traversal_Tree(root.left)
            self.Depth_First_Traversal_Tree(root.right)





if __name__=="__main__":
    # Assignment-1: implement the BFT using tree data structure
    # Assignment-2: convert the bft search method to Breadth First Search where user passes a value and
    #
    # Using a Python dictionary to act as an adjacency list

    #=========== using tree data structure
    #               [20]
    #           [10]     [21]
    #       [9      [15]      [30]
    #     [N N]  [14] [18]   [25 N]
    #           [N N] [N N] [24    28]
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
    root.Depth_First_Traversal_Tree(root)
    #implement the search method



