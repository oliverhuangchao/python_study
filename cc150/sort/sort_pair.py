# sort with pair
# height should be smaller than after
# wight should be smaller than after
# print all the possible combination


class person:
	def __init__(self,h,w):
		self.h = h
		self.w = w


def dfs(res,path,peoples,pos):
	size = len(peoples)
	if pos == size:
		res.append(path)
		return
	for i in range(pos,size):
		if not path or peoples[i].w > path[-1].w:
			dfs(res,path+[peoples[i]],peoples,i+1)



def sortPair(peoples):
	peoples.sort(key = lambda x:x.h)
	res = []
	dfs(res,[],peoples,0)
	return res


nums = [(65,80),(70,150),(56,90)]#(75,190),(60,95),(68,110)]
peoples = map(lambda x:person(x[0],x[1]),nums)
res = sortPair(peoples)
for i in res:
	print len(i)

