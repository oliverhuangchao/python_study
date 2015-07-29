#import mylist as ll
import pdb
#sort a stack


def sort_stack(s1):
    s2 = []
    tmp = 0
    while s1:
        tmp = s1.pop()
        while s2 and tmp > s2[-1]:
            s1.append(s2.pop())
        s2.append(tmp)
    while s2:
        s1.append(s2.pop())
    return



a = [3,2,1,4,5,2,1,2,3,4,1,2,43,1,23,1,1,3]
print a
sort_stack(a)
print a
