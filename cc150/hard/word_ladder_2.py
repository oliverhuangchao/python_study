import collections
import string
def findLadders(start, end, worddict):
    # write your code here
    worddict.add(end)
    level = {start}
    size = len(start)
    parent = collections.defaultdict(set)
    while level and end not in parent:
        next_level = collections.defaultdict(set)
        for node in level:
            for char in string.ascii_lowercase:
                for i in range(size):
                    newnode = node[:i]+char+node[i+1:]
                    if newnode in worddict and newnode not in parent:
                        next_level[newnode].add(node)
        level = next_level
        parent.update(next_level)
    res = [[end]]
    print parent[res[0][0]]
    while res and res[0][0] != start:
        res = [[p] + r for r in res for p in parent[r[0]]]
    return res


start = "hit"
end = "cog"
worddict = set(["hot","dot","dog","lot","log"])
print findLadders(start,end,worddict)