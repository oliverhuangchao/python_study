import pdb
import collections
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def change(root, value):
    z = []
    p = root
    while root or z:
        while root:
            z.append(root)
            #if root.val >= value:
            root.val += value
            root = root.left
        root = z.pop().right
    root = p

def generateTrees(n):
    res = []
    if n==0:
        res.append(None)
        return res
   
    for i in range(1,n+1):
        #pdb.set_trace()
        #root = TreeNode(i)
        #if n == 3:
        #    pdb.set_trace()
        left = generateTrees(i-1)
        right = generateTrees(n-i)
        #if n == 3:
        #    pdb.set_trace()
        for k in right:
            change(k,i)
        for x in left:
            for y in right:
                root = TreeNode(i)
                root.left = x
                root.right = y
                res.append(root)
    return res


if __name__=='__main__':
    res = generateTrees(5)
    print res
    for i in res:
        print level_tranversal(i)

