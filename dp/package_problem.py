import pdb
# back pack problem
# solved using dfs
def dfs(m,pos,res,max_value,max_size):
    #pdb.set_trace()
    if res > max_size:
        res -= m[pos-1]
        #if res == 10:
        #    pdb.set_trace()
        max_value[0] = max(max_value[0],res)
        return
    for i in range(pos,len(m)):
        dfs(m,i+1,res+m[i],max_value,max_size)
        
def dfs_backPack(m, A):
    A.sort(reverse = True)
    A.append(m+1)
    print A
    max_value = [0]
    dfs(A,0,0,max_value,m)
    return max_value[0]



# using dp solution

#def 
def dp_backPack(m,w):
    w.sort()
    f = [False for i in range(m+1)]
    f[0] = True
    for i in range(len(w)):
        for j in range(m,-1,-1):
            if j >= w[i] and f[j-w[i]]:
                f[j] = f[j-w[i]]
            
    res = m
    for item in f[::-1]:
        if item:
            break
        res -= 1
    return res


#w = [3,4,5,8]
w = [81,112,609,341,164,601,97,709,944,828,627,730,460,523,643,901,602,508,401,442,738,443,555,471,97,644,184,964,418,492,920,897,99,711,916,178,189,202,72,692,86,716,588,297,512,605,209,100,107,938,246,251,921,767,825,133,465,224,807,455,179,436,201,842,325,694,132,891,973,107,284,203,272,538,137,248,329,234,175,108,745,708,453,101,823,937,639,485,524,660,873,367,153,191,756,162,50,267,166,996,552,675,383,615,985,339,868,393,178,932]
m = 80000
print dp_backPack(m,w)
