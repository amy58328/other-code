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
		i=2.5
		node = []
		xi = []
		while i <= 7.5:
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

def neuton_divided_difference():
	fi = []
	fi.append(fx)
	index = 0
	time = 1;
	
	while len(fi[index]) != 1:
		temparr = []
		for i in range(0,len(fi[index])-1):
			temp = fi[index][i+1] - fi[index][i]
			temp /= (x[i+time] - x[i])
			print(temp,end =  " ")
			temparr.append(temp)
		time += 1
		fi.append(temparr)
		index += 1

		i = 2.5
		while i <= 7.5:
			i+=0.001


	



# 老師實驗數據
# Lagrange
# Lagrange()
neuton_divided_difference()