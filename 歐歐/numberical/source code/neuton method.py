import numpy as np
import random
import math

output = open("neuton method.out", "w")

def fun1(x):
	return math.exp(x) - 3*x*math.cos(2*x) - 8.3
def dif1(x):
	return math.exp(x) - 3*math.cos(2*x) + 6*x*math.sin(2*x)
def fun2(x):
	return math.exp(x*math.sin(x)) - x*math.cos(2*x) - 2.8
def dif2(x) :
	return math.exp(x*math.sin(x))*x*math.cos(x) + math.exp(x*math.sin(x))*math.sin(x) + 2*x*math.sin(2*x) - math.cos(2*x)
def fun3(x):
	return x*math.cos(2*x) + math.exp(x) - 2.3
def dif3(x):
	return math.exp(x) - 2*x*math.sin(2*x) + math.cos(2*x)
def fun4(x):
	return math.exp(math.cos(x)) + math.cos(x) - 1.1	
def dif4(x):
	return (-math.sin(x)) * (math.exp(math.cos(x)) + 1)


print("f(x) = exp(x) - 3*x*cos(2*x) - 8.3",file = output)
print("range of x is [-10,2]",file = output)
print(file = output)
t = 0
e = 0.00000001;

while t != 10 :
	times = 0
	a = random.randint(-10,2)
	t = t+1
	print("test",t,":",file = output)

	print("a =",a,file = output)

	while 1 :
		times = times + 1
		c = -(fun1(a)/dif1(a))
		a = a + c

		if abs(c) < e or times > 500:
			print("times =",times,"=>",c,file = output)
			print(file = output)
			break

			
print("------------------------------------------",file = output)
print(file = output)

print("f(x) = exp(x*sin(x)) - x*cos(2*x) - 2.8",file = output)
print("range of x is [-5,5]",file = output)
print(file = output)

t = 0

while t != 5 :
	times = 0
	a = random.randint(-5,5)
	t = t+1
	print("test",t,":",file = output)

	print("a =",a,file = output)

	while 1 :
		times = times + 1
		c = -(fun2(a)/dif2(a))
		a = a + c

		if abs(c) < e or times > 500:
			print("times =",times,"=>",c,file = output)
			print(file = output)
			break

print("------------------------------------------",file = output)
print(file = output)

print("f(x) = x*math.cos(2*x) + math.exp(x) - 2.3",file = output)
print("range of x is [-10,1]",file = output)
print(file = output)

t = 0

while t != 5 :
	times = 0
	a = random.randint(-10,1)
	t = t+1
	print("test",t,":",file = output)

	print("a =",a,file = output)

	while 1 :
		times = times + 1
		c = -(fun3(a)/dif3(a))
		a = a + c

		if abs(c) < e or times > 500:
			print("times =",times,"=>",c,file = output)
			print(file = output)
			break

print("------------------------------------------",file = output)
print(file = output)

print("f(x) = math.exp(math.cos(x)) + math.cos(x) - 1.1",file = output)
print("range of x is [5,10]",file = output)
print(file = output)

t = 0

while t != 5 :
	times = 0
	a = random.randint(5,10)
	t = t+1
	print("test",t,":",file = output)

	print("a =",a,file = output)

	while 1 :
		times = times + 1
		c = -(fun4(a)/dif4(a))
		a = a + c

		if abs(c) < e or times > 500:
			print("times =",times,"=>",c,file = output)
			print(file = output)
			break