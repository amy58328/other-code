import numpy as np
import random
import math

output = open("Besection method.out", "w")

def fun1(x):
	return math.exp(x) - 3*x*math.cos(2*x) - 8.3
def fun2(x):
	return math.exp(x*math.sin(x)) - x*math.cos(2*x) - 2.8
def fun3(x):
	return x*math.cos(2*x) + math.exp(x) - 2.3
def fun4(x):
	return math.exp(math.cos(x)) + math.cos(x) - 1.1

print("f(x) = exp(x) - 3*x*cos(2*x) - 8.3",file = output)
print("range of x is [-10,2]",file = output)
print(file = output)
t = 0
e = 0.00000001;

while(t != 10) :
	times = 0
	a = random.randint(-10,2)
	b = random.randint(-10,2)

	if fun1(a)*fun1(b) < 0 :
		t = t+1
		print("test",t,":",file = output)

		print("a =",a,file = output)
		print("b =",b,file = output)

		while abs(a-b) >= 2 * e :
			times = times + 1
			c = (a+b)/2

			if fun1(c) == 0 :
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			if fun1(a)*fun1(c) < 0 :
				b = c
			else :
				a = c

		print("times =",times,"=>",c,file = output)
		print(file = output)
			
print("------------------------------------------",file = output)
print(file = output)

print("f(x) = exp(x*sin(x)) - x*cos(2*x) - 2.8",file = output)
print("range of x is [-5,5]",file = output)
print(file = output)

t = 0

while(t != 10) :
	times = 0
	a = random.randint(-5,5)
	b = random.randint(-5,5)

	if fun2(a)*fun2(b) < 0 :
		t = t+1
		print("test",t,":",file = output)

		print("a =",a,file = output)
		print("b =",b,file = output)

		while abs(a-b) >= 2 * e :
			times = times + 1
			c = (a+b)/2

			if fun2(c) == 0 :
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			if fun2(a)*fun2(c) < 0 :
				b = c
			else :
				a = c

		print("times =",times,"=>",c,file = output)
		print(file = output)

print("------------------------------------------",file = output)
print(file = output)

print("f(x) = x*math.cos(2*x) + math.exp(x) - 2.3",file = output)
print("range of x is [-10,1]",file = output)
print(file = output)

t = 0

while(t != 10) :
	times = 0
	a = random.randint(-10,1)
	b = random.randint(-10,1)

	if fun3(a)*fun3(b) < 0 :
		t = t+1
		print("test",t,":",file = output)

		print("a =",a,file = output)
		print("b =",b,file = output)

		while abs(a-b) >= 2 * e :
			times = times + 1
			c = (a+b)/2

			if fun3(c) == 0 :
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			if fun3(a)*fun3(c) < 0 :
				b = c
			else :
				a = c

		print("times =",times,"=>",c,file = output)
		print(file = output)

print("------------------------------------------",file = output)
print(file = output)

print("f(x) = math.exp(math.cos(x)) + math.cos(x) - 1.1",file = output)
print("range of x is [5,10]",file = output)
print(file = output)

t = 0

while(t != 10) :
	times = 0
	a = random.randint(5,10)
	b = random.randint(5,10)

	if fun4(a)*fun4(b) < 0 :
		t = t+1
		print("test",t,":",file = output)

		print("a =",a,file = output)
		print("b =",b,file = output)

		while abs(a-b) >= 2 * e :
			times = times + 1
			c = (a+b)/2

			if fun4(c) == 0 :
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			if fun4(a)*fun4(c) < 0 :
				b = c
			else :
				a = c

		print("times =",times,"=>",c,file = output)
		print(file = output)