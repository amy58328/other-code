import numpy as np
import math
import random
import matplotlib.pyplot as plt

x = []
fx = []
factorial = []
customize_x = []
customize_fx = []
node = []
xi = []
def create_factorial():
	for i in range(1,101):
		temp = 1
		for j in range(1,i):
			temp *= j
		factorial.append(temp)
	
def readfile(filename):
	file = open(filename, 'r')
	for i in file.readlines():
		a,b = i.split()
		x.append(float(a))
		fx.append(float(b))

def Lagrange():
		i=2.4
		node.clear()
		xi.clear()
		while i <= 8.12:
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

def cal_neuton(number,fi,index):
	n = fi[0][0]
	for i in range(1,index+1):
		temp = fi[i][0]
		for j in range(0,i):
			temp *= (number - x[j])
		n += temp
	return n 

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
			temparr.append(temp)
		time += 1
		fi.append(temparr)
		index += 1

	i = 2.4
	node.clear()
	xi.clear()
	while i <= 8.12:
		temp = cal_neuton(i,fi,index)
		node.append(temp)
		xi.append(i)
		i+=0.001
	plt.title("neuton_divided_difference")
	plt.plot(xi,node)
	plt.show()

def cal_forward(number,fi,index):
	s = (number - x[0])/(x[1] - x[0])

	n = fi[0][0]
	for i in range(1,index+1):
		temp = fi[i][0]
		for j in range(0,i):
			temp *= (s - j)
		temp /= factorial[i]
		n += temp
	return n 

def cal_backward(number,fi,index):
	s = (number - x[len(fi[0])-1])/(x[1] - x[0])

	n = fi[0][len(fi[0])-1]

	for i in range(1,index+1):
		temp = fi[i][len(fi[i])-1]
		for j in range(0,i):
			temp *= (s + j)
		temp /= factorial[i]
		n += temp
	return n 

def forward():
	fi = []
	fi.append(fx)
	index = 0
	time = 1;
	
	# build table
	while len(fi[index]) != 1:
		temparr = []
		for i in range(0,len(fi[index])-1):
			temp = fi[index][i+1] - fi[index][i]
			temparr.append(temp)
		time += 1
		fi.append(temparr)
		index += 1

	node.clear()
	xi.clear()
	i = 2.4
	while i <= 8.1:
		temp = cal_forward(i,fi,index)
		node.append(temp)
		xi.append(i)
		i += 0.001
	plt.title("forward")
	plt.plot(xi,node)
	plt.show()	 

def backward():
	fi = []
	fi.append(fx)
	index = 0
	time = 1;
	
	# build table
	while len(fi[index]) != 1:
		temparr = []
		for i in range(0,len(fi[index])-1):
			temp = fi[index][i+1] - fi[index][i]
			temparr.append(temp)
		time += 1
		fi.append(temparr)
		index += 1

	node.clear()
	xi.clear()

	i = 2.4
	while i <= 8.1:
		temp = cal_backward(i,fi,index)
		node.append(temp)
		xi.append(i)
		i += 0.001
	plt.title("backword")
	plt.plot(xi,node)
	plt.show()

def creat_UNEquidistant_data(diff):
	for i in range(0,30):
		x.append(random.uniform(0,10))
	
	for i in x:
		if diff == 1:
			temp = 3 * i * math.cos(2*i) - 3*i
		elif(diff == 2) :
			temp = math.sin(3*i) + 2 -  math.exp(i)
		elif(diff == 3):
			temp = math.exp(pow((i-5),2)) - math.sin(3*(i+12))-5
		fx.append(temp)

def customize_function_create(diff):
	i = 0
	while i<= 10:
		customize_x.append(i)
		if diff == 1:
			temp = 3 * i * math.cos(2*i) - 3*i
		elif(diff == 2): #sin(3x)+2-exp(x)
			temp = math.sin(3*i) + 2 -  math.exp(i)
		elif(diff == 3):
			temp = math.exp(pow((i-5),2)) - math.sin(3*(i+12))-5

		customize_fx.append(temp)
		i += 0.0001

def compare(name):
	plt.title("compare")
	plt.plot(customize_x,customize_fx,color = 'blue',label = "f(x)")
	plt.plot(xi,node,color='green',label = name)
	plt.legend(loc='upper right')
	plt.show()

def creat_Equidistant_data(diff):
	i = 0
	while i <= 10:
		if(diff == 1):
			temp = 3 * i * math.cos(2*i) - 3*i
		elif(diff == 2): #sin(3x)+2-exp(x)
			temp = math.sin(3*i) + 2 -  math.exp(i)
		elif(diff == 3):
			temp = math.exp(pow((i-5),2)) - math.sin(3*(i+12))-5
		fx.append(temp)
		x.append(i)
		i+=0.5



# 老師實驗數據
# readfile('Equidistant.txt')
# Lagrange()
# neuton_divided_difference()

# x.clear()
# fx.clear()

create_factorial()
# readfile('unEquidistant.txt')
# forward()
# backward()

#customize function 
# 1. 3x*cos(2x)-3x
# customize_function_create(1)
# x.clear()
# fx.clear()
# creat_UNEquidistant_data(1)
# Lagrange()
# compare("Lagrange")
# neuton_divided_difference()
# compare("neuton_divided_difference")

# x.clear()
# fx.clear()
# creat_Equidistant_data(1)
# forward()
# compare("forward")
# backward()
# compare("backward")

# # 2. sin(3x)+2-exp(x)
# customize_fx.clear()
# customize_x.clear()
# customize_function_create(2)
# x.clear()
# fx.clear()
# creat_UNEquidistant_data(2)
# Lagrange()
# compare("Lagrange")
# neuton_divided_difference()
# compare("neuton_divided_difference")

# x.clear()
# fx.clear()
# creat_Equidistant_data(2)
# forward()
# compare("forward")
# backward()
# compare("backward")


# 3.exp((x-5)^2)-sin(3(x+12))-5
customize_fx.clear()
customize_x.clear()
customize_function_create(3)
x.clear()
fx.clear()
creat_UNEquidistant_data(3)
Lagrange()
compare("Lagrange")
neuton_divided_difference()
compare("neuton_divided_difference")

x.clear()
fx.clear()
creat_Equidistant_data(3)
forward()
compare("forward")
backward()
compare("backward")
