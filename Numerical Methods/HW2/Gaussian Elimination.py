import numpy as np

n = 3;
# uniform -> random
# randint -> int
A = np.random.randint(1,100,[n,n])
b = np.random.randint(1,100,[n,1])
ans = np.zeros((n,1))

print(A)
print(b)


for j in range(0,n-1):
	for i in range(j+1,n):
		mul = A[i][j] / A[j][j]
		A[i][j] -= A[j][j] * mul
		A[i][i] -= A[j][i] * mul
		b[i][0] -= b[j][0] * mul

print(A)
print(b)


for i in range(n-1,0,-1):
	temp = 0
	for j in range(1,n):
		temp += 
	ans[i][0] = b[i][0] / A[i][n-1];
# 	for j in range(n-1,0,-1):

ans[n-1][0] = b[n-1][0] / A[n-1][n-1];
print(ans[n-1][0])