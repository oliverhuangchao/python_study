import collections
import pdb
class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

# inorder tranversal
def inorder(root):
    stack = []
    res = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        tmp = stack.pop()
        res.append(tmp.val)
        root = tmp.right
    return res


def levelOrder(root):
    parent = collections.deque()
    children = collections.deque()
    res = []
    if root is None:
        return res
    res.append([])
    res[0].append(root.val)
    parent.append(root)
    while parent:
        root = parent.popleft()
        if root.left:
            children.append(root.left)
        if root.right:
            children.append(root.right)
        if not parent:
            if children:
                res.append([])
            while children:
                tmp = children.popleft()
                parent.append(tmp)
                res[-1].append(tmp.val)
    
    return res



x1 = TreeNode(2)
x2 = TreeNode(1)
x3 = TreeNode(3)
x1.left = x2
x1.right = x3


#res = inorder(x1)
res = levelOrder(x1)
print res