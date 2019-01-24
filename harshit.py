class Node:
    def __init__(self,value):
        '''
        Objective: It will initialize the the instance variables of the class.
        '''
        self.data=value
        self.left=None
        self.right=None


class BTree():
    def __init__(self):
        '''
        Objective:It will initialize the the instance variables of the class.
        '''
        self.head=None
        
    def Insert(self,value):
        '''
        Objective: It will insert the value into the Binary Tree.
        Input: Value=Value to be inserted into the Binary Tree.
        '''

        if self.head==None:
            node=Node(value)
            self.head=node
        else:
            node=Node(value)
            
            if value<self.data:
                if self.left==None:
                    node.left=Node(value)
                else:
                    node.right.Insert()
        
print("hello world")
