#valid parathesis
def rec(n,left,right,res,path):
	if left > n:
		return 
	if left == n and right == n:
		res.append(path)
		return
	if left == right:
		rec(n,left+1,right,res,path+['('])
	else:
		rec(n,left+1,right,res,path+['('])
		rec(n,left,right+1,res,path+[')'])

def print_parathesis(n):
	res = []
	path = []
	rec(n,0,0,res,path)
	return res

res = print_parathesis(3)
for i in res:
	print ''.join(i)