import pdb

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Line:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        #self.c = c
  
    def check_point(self,p):
        if p.x - self.a.x == 0:
            if p.x-self.b.x !=0:
                return False
            else:
                return True
        if p.x - self.b.x ==0:
            if p.x-self.a.x != 0:
                return False
            else:
                return True
                
        if float((p.y-self.a.y))/(p.x-self.a.x) != float((p.y-self.b.y))/(p.x-self.b.x):
            return False
        else:
            return True

    def in_check(self,p):
        if p.x == self.a.x and p.y == self.a.y:
            return True
        if p.x == self.b.x and p.y == self.b.y:
            return True
        return False
        
        
        
def point_str(x):
    return str(x.x)+'*'+str(x.y)


# @param {int[]} points an array of point
# @return {int} an integer
def maxPoints(points):
    # Write your code here
#    pdb.set_trace()
    size = len(points)
    if size<2:
        return size
    res = 0
    for i in range(size):
        for j in range(i+1,size):
            count = 0
            if points[i].x == points[j].x and points[i].y == points[j].y:
                res = max(check[point_str(points[i])],check[point_str(points[j])])-2
                continue;
            tmp_line = Line(points[i],points[j])
            for k in range(size):
                if i==k or j==k:
                    continue;
                if tmp_line.check_point(points[k]):
                    count += 1

           
            if i == 3:
                print max(check[point_str(points[i])],check[point_str(points[j])])
            res = max(count,res)


    return res+2

#x = [[1,1],[1,1],[1,1]]
x = [[0,-12],[5,2],[2,5],[0,-5],[1,5],[2,-2],[5,-4],[3,4],[-2,4],[-1,4],[0,-5],[0,-8],[-2,-1],[0,-11],[0,-9]]
#x = [[5,2],[0,-5],[0,-8]]
points = map(lambda x:Point(x[0],x[1]),x)
z = map(lambda x:str(x.x)+'*'+str(x.y),points)
check = dict()
for item in z:
    if item in check:
        check[item] += 1
    else:
        check[item] = 1

print check

#print points
print maxPoints(points)

