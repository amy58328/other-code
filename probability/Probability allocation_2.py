import numpy as np
import random
import matplotlib.pyplot as plt

num = []
x = []
num_amount = []
test_amount = []

def init():
	for i in range(0,31):
		test_amount[i] = 0

for i in range(130,161):
	x.append(i)
	num_amount.append(0)
	test_amount.append(0)

for i in range(0,100000):
	temp = random.randint(130,160)
	num.append(temp)
	temp -= 130
	num_amount[temp] += 1

plt.title("Random data distribution of 100,000 records")
plt.bar(x,num_amount)
plt.show()


t = 10

while t :
	t -= 1
	init()
	spacing = random.randint(10,80)
	index = 0
	temp = 0
	while(index < 100000):
		temp += num[index]
		if(index % spacing == spacing-1 and index !=0):
			temp /=spacing
			temp = round(temp)
			temp -= 131	
			test_amount[temp] += 1
			temp = 0
		index += 1
	spacing = str(spacing)
	plt.title("Random data distribution,number of Section:"+ spacing)
	plt.bar(x,test_amount)
	plt.show()




