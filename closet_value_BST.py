class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data
        
    def indorder(self):
        if self.left:
            self.left.indorder()
        print(self.data)
        if self.right:
            self.right.indorder()
    
    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
def closet(root,data):
    a = root.data
    kid = root.left if root.data>data else root.right
    if not kid:
        return a
    b = closet(kid,data)
    return (min(a,b,key = lambda x: abs(data - x)))
            
            
            
            
            
r = Node(8)
r.insert(70)
r.insert(1)
r.insert(35)
r.insert(5)
r.indorder()
r.preorder()
res = closet(r,9)
print(res)

