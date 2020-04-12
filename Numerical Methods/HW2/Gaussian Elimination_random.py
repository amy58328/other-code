import numpy as np
import sys

for n in range(2,100):
	# uniform -> random
	# randint -> int

	print("=====================================")
	print("n=",n)
	A = np.random.randint(1,100,[n,n])
	b = np.random.randint(1,100,n)
	ans = np.zeros(n)

	print("A=",A)
	print("b=",b)

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
		continue
	if(flag == 2):
		print("Infinite Solutions")
		continue

	for i in range(n-1,-1,-1):
		temp = 0
		for j in range(n-1,i,-1):
			temp += A[i][j] * ans[j]
		ans[i] = (b[i] - temp)/A[i][i]


	# print()
	print("ans=",ans)