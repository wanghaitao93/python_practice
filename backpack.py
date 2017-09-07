import sys

w = map(int, sys.stdin.readline().strip().split())
v = map(int, sys.stdin.readline().strip().split())
n = int(sys.stdin.readline().strip())
cap = int(sys.stdin.readline().strip())

# two dimension
# http://blog.sina.com.cn/s/blog_3fe961ae0100zap7.html#cmt_516417EC-7F000001-7EF3D1DB-822-8A0
arr = [[0 for i in range(cap+1)] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, cap+1):
        arr[i][j] = arr[i-1][j]
        if j >= w[i-1] and arr[i-1][j-w[i-1]] + v[i-1] > arr[i][j]:
            arr[i][j] = arr[i-1][j-w[i-1]] + v[i-1]
print arr[-1][-1] 

# one dimension
f = [-1 for i in range(cap+1)]
f[0] = 0
for i in range(n):
    for j in range(cap,w[i]-1,-1):
	if f[j-w[i]] != -1:
	    f[j] = max(f[j],f[j-w[i]] + v[i])
print max(f)
