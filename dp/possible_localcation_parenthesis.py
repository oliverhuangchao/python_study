# all possible result for an expression
# such as for express "2*3-4*5"
# three will be many result based on the location of parenthesis, eg. "2*(3-4)*5"
# print all the possible result given a express

import pdb

op_dict = {'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y, '/':lambda x,y:x/y}


# given two list of integers, make a combination result based on op
def combination(list1,list2,op):
    res = []
    for i in list1:
        for j in list2:
            res += [op_dict[op](i,j)]
    return res


# split the expression into two parts, each part use a recursive function to achieve

def rec(exp):
    try:
        return [int(exp)]
    except:
        size = len(exp)
        if size == 0:
             return []
        res = []
        i = 0
        while i < size:
            if exp[i] >= '0' and exp[i] <= '9':
                i += 1
                continue
            first = rec(exp[:i])
            #print first
            second = rec(exp[i+1:])
            #print second
            op = exp[i]
            res += combination(first,second,op)
            i += 1
        return res



#res = combination([1,2,3],[4,5,6],'+')
exp = "10+5*2"
res = rec(exp)
print res
