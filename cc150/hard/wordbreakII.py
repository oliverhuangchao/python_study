# find word break number
def wordbreak(wordDict,z,x):
	size = len(z)
	x[0] = True
	for i in range(1,size+1):
		for j in range(i):
			if x[j] and z[j:i] in wordDict:
				x[i] = True
				break
	#return x[size]

# find the how to break
# check something if already visited

def dfs(ori,x,wordDict,pos,res,path,visited):
	if pos == len(ori):
		res.append(path)
		return True
	# visited is quite important, we need to know whether this postion is defintely a wrong way or not.
	# at first, nobody knows, but once a tranversal get it and know it is wrong
	# we need to avoid this way next time
	if not visited[pos]:
		return

	visited[pos] = False
	for i in range(pos,len(ori)):
		if x[i] and ori[pos:i+1] in wordDict:
			visited[pos] = dfs(ori,x,wordDict,i+1,res,path+[ori[pos:i+1]],visited)
	return visited[pos]

def wordbreak2():
	#wordDict = set(["cat", "cats", "and", "sand", "dog"])
	wordDict = set(["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
	#z = 'catsanddog'
	z = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
	x = [False for i in range(len(z)+1)]
	wordbreak(wordDict,z,x)
	del x[0]
	res = []
	visited = [True for i in range(len(z))]
	#print x
	dfs(z,x,wordDict,0,res,[],visited)
	print res
	#print x

wordbreak2()



