# nqueen 问题
# 关键点是如何判断重复
# 两个对角线是关键的问题
# 空间复杂度是O(n)

check_cols = set()
check_diag_1 = set()
check_diag_2 = set()

def point2line(num,N):
  res = ['.' for i in range(N)]
  res[num] = 'Q'
  return ''.join(res)
  
def transform(path,N):
  res = []
  for k in path:
      append(point2line(k,N))
  return res

def dfs(res,path,step_row,N):
  if step_row == N:
      res.append(transform(path,N))
      return
  for i in range(N):
      if i not in check_cols and i+step_row not in check_diag_1 and i-step_row not in check_diag_2:
          check_cols.add(i)
          check_diag_1.add(i+step_row)
          check_diag_2.add(i-step_row)
          dfs(res,path+[i],step_row+1,N)
          check_cols.remove(i)
          check_diag_1.remove(i+step_row)
          check_diag_2.remove(i-step_row)
          
  

def solveNQueens(n):
  # write your code here
  res = []
  if n == 0:
      return res
  dfs(res,[],0,n)
  return res

