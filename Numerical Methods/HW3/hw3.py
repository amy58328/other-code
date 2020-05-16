import numpy as np
import matplotlib.pyplot as plt

file = open('HW3.txt','r')

x = []
fx = []


for i in file.readlines():
	a,b = i.split()
	x.append(float(a))
	fx.append(float(b))

def Lagrange():
		i=0
		node = []
		xi = []
		while i <= 10:
			
			fi = 0
			for j in range(0,len(x)):
				temp = 1;
				for k in range(0,len(x)):
					if(k != j):
						temp *= (i-x[k]) / (x[j]-x[k]);
				temp *= fx[j]
				fi += temp;
			# print(fi);
			node.append(fi)
			xi.append(i)
			i+=0.001
		plt.title("Lagrange")
		plt.plot(xi,node)
		plt.show()

# Lagrange
Lagrange()