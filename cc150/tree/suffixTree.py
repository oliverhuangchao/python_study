# implement a suffixTree
# this basic structure can be recited 

import pdb
class suffixTree:
	def __init__(self,s):
		self.root = suffixTreeNode()
		for i in range(len(s)):
			suffix = s[i:]
			self.root.insertString(suffix,i)


class suffixTreeNode:
	def __init__(self):
		self.children = dict()
		self.value = ''
		self.indexes = []# index is quite important

	def insertString(self,s,i):
		self.indexes.append(i)
		if s:
			value = s[0]
			if value in self.children:
				child = self.children[value]
			else:
				child = suffixTreeNode()
				self.children[value] = child
			child.insertString(s[1:],i)

	def searchString(self,s):
		if not s:
			return self.indexes
		else:
			first_char = s[0]
			if first_char in self.children:
				remainder = s[1:]
				return self.children[first_char].searchString(remainder)
		return None


if __name__ == '__main__':
	sft = suffixTree('chaoh')
	print sft.root.searchString('h')
	#print sft.root.children['a'].indexes







	