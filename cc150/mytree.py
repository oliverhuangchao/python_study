import collections
# tree basic structure

# construct a tree using a array
#

class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right= None



def build_tree(nums):
    root = TreeNode(int(nums[0]))
    parent = collections.deque()
    parent.append(root)
    i = 1
    size = len(nums)
    while parent and i<size:
        tmp = parent.popleft()
        if nums[i] != '#':
            tmp.left = TreeNode(int(nums[i]))
            parent.append(tmp.left)
        i += 1
        if i >= size:
            break
        if nums[i] != '#':
            tmp.right = TreeNode(int(nums[i])) 
            parent.append(tmp.right)
        i+= 1
        
    return root


def inorder_tranversal(root):
    a = root
    if not a:
        return []
    z = []
    res = []
    while a or z:
        while a:
            z.append(a)
            a = a.left
        tmp = z.pop()
        res.append(tmp.val)
        a = tmp.right
    return res

# pre order tranversal
def preorder_tranversal(root):
    a = root
    if not a:
        return []
    z = []
    res = []
    while a or z:
        while a:
            z.append(a)
            res.append(a.val)
            a = a.left
        tmp = z.pop()
        a = tmp.right
    return res

#post tranversal
def postorder_tranversal(root):
    p = root
    if not p:
        return []
    z = []
    res = []
    q = None
    while True:
        while p:
            z.append(p)
            p = p.left
        q = None
        while z:
            p = z.pop()
            if p.right == q:
                res.append(p.val)
                q = p
            else:
                z.append(p)
                p = p.right
                break
        if not z:
            break

