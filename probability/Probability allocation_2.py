import numpy as np
import matplotlib.pyplot as mat
import random 

height = []
x = []

for i in range(130,161):
	x.append(i)

print(x)
for i in range(0,1000005):
	temp = random.randint(130,160)
	height.append(temp)

t = 10

while(t):
	t -= 1
	amo = random.randint(10,80)
