import numpy as np
import random
import math

output = open("fixed point method.out", "w")

def log1(x):
    return math.log(3*x*math.cos(2*x) + 8.3)
def log2(x):
	return math.log(x*math.cos(2*x)+2.8)/math.sin(x) * math.log(math.exp(1))
def log3(x):
	return math.log(x*math.cos(2*x) + math.exp(x) - 2.3)
def log4(x):
	return math.log(math.exp(math.cos(x)) + math.cos(x) - 1.1)

print("f(x) = exp(x) - 3*x*cos(2*x) - 8.3",file = output)
print("range of x is [-10,2]",file = output)
print(file = output)
t = 0
e = 0.00000001;

while t != 5 :
	times = 0
	c = random.randint(-10,2)

	if c != -3 and c != -6 and c != -9 and c != -10:
		t = t+1
		print("test",t,":",file = output)
		print("c =",c,file = output)
		while 1 :
			times = times + 1
			old_c = c
			c = log1(c)

			if abs(c-old_c) < e :
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			if times > 500 :
				print("can't find",file = output)
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
	c = random.randint(-5,5)

	if c != 1 and c != 0 and c != 2 and c != -3 and c != -5 and c != 3 and c != 5 and c != -4:
		t = t+1
		print("test",t,":",file = output)
		print("c =",c,file = output)
		while 1 :
			times = times + 1
			old_c = c
			c = log2(c)

			if abs(c-old_c) < e :
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			if times > 500 :
				print("can't find",file = output)
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
	c = random.randint(-10,1)

	if c != -2 and c != -9 and c != -3 and c != -8 and c != -10 and c != -4 and c != -6 and c != -1 and c != -5 and c != 0 and c != 1 and c != -7 :
		t = t+1
		print("test",t,":",file = output)
		print("c =",c,file = output)
		while 1 :
			times = times + 1
			old_c = c
			c = log3(c)

			if abs(c-old_c) < e :
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			if times > 500 :
				print("can't find",file = output)
				print(file = output)
				break

	print("can't find",file = output)
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
	c = random.randint(5,10)

	if c != 9 and c != 8 and c != 10 :
		t = t+1
		print("test",t,":",file = output)
		print("c =",c,file = output)
		while 1 :
			times = times + 1
			old_c = c
			c = log4(c)

			if abs(c-old_c) < e :
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			if times > 500 :
				print("can't find",file = output)
				print(file = output)
				break