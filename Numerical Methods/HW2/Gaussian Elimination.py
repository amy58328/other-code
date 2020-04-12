import numpy as np
import sys

n = 3;
# uniform -> random
# randint -> int
A = np.array([[2,3,4,],[4,6,8],[1,2,3]])
b = np.random.randint(1,100,n)
ans = np.zeros(n)

print(A)
print(b)

flag = 0
for j in range(0,n-1):
	for i in range(j+1,n):
		if(A[j][j] == 0 and b[i] != b[j]):
			flag = 1
			break
		if(A[j][j] == 0 and b[i] == b[j]):
			flag = 2
			break
		mul = A[i][j] / A[j][j]
		A[i][j] -= A[j][j] * mul
		A[i][i] -= A[j][i] * mul
		b[i] -= b[j] * mul

if(flag == 1):
	print("No Solution")
	sys.exit()
if(flag == 2):
	print("Infinite Solutions")
	sys.exit()
print(A)
print(b)


for i in range(n-1,-1,-1):
	temp = 0
	for j in range(n-1,i,-1):
		temp += A[i][j] * ans[j]
	ans[i] = (b[i] - temp)/A[i][i]



ans[n-1] = b[n-1] / A[n-1][n-1];
print(ans[n-1])

# print()
print(ans)