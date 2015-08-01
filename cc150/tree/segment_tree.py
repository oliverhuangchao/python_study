class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None


class SegmentTree:
	def __init__(self):
		root = None
	# build segment tree
	def build(self, start, end):
	    # write your code here
	    if start > end:
	        return None
	    root = SegmentTreeNode(start,end)
	    if start < end:
	        mid = (start+end)/2
	        root.left = self.build(start,mid)
	        root.right =self.build(mid+1,end)
	    return root

	 # 