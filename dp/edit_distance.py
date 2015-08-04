# edit distance
# suppose three operation has the same cost
# if it is not the same cost, change code in line:19. treat three operation seperately

def minDistance(s, t):
    # write your code here
    z1 = len(s)
    z2 = len(t)
    f = [[0 for j in range(z1+1)] for j in range(z2+1)]
    for j in range(1,z1+1):
        f[0][j] = f[0][j-1] + 1
    for i in range(1,z2+1):
        f[i][0] = f[i-1][0] + 1
    for i in range(1,z2+1):
        for j in range(1,z1+1):
            if s[j-1] == t[i-1]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = min([f[i-1][j],f[i][j-1],f[i-1][j-1]])+1
    return f[z2][z1]



if __name__=='__main__':
    print minDistance('hello','chaoh')