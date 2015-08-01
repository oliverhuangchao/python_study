# airplanes in the sky
import pdb
import heapq
class intervals:
    def __init__(self,start,end):
        self.start = start
        self.end = end




def countOfAirplanes(airplanes):
    # write your code here
    airplanes.sort(key=lambda x:x.start)
    if not airplanes:
        return 0
    z = [airplanes[0].end] #use z as a stack
    res = 1
    #pdb.set_trace()
    for i in airplanes[1:]:
        #print z[0]
        while z and i.start >= z[0]:
            heapq.heappop(z)
        heapq.heappush(z,i.end)
        #print z
        res = max(res,len(z))
    return res


airplanes = map(lambda x:intervals(x[0],x[1]),[(1,10),(2,3),(5,8),(4,7)])
print countOfAirplanes(airplanes)

# x =  [3,2,1,4,5]
# z = []
# for i in x:
#     heapq.heappush(z,i)
# print z[0]