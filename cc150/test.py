import mytree as tr



nums = map(lambda x:str(x),[1,2,3,4,5,6,7])
print nums
root = tr.build_tree(nums)

inorder = tr.inorder_tranversal(root)
print inorder
postorder = tr.postorder_tranversal(root)
print postorder
preorder = tr.preorder_tranversal(root)
print preorder
