import numpy as np
import random
import math

output = open("modify false position.out", "w")

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

while t != 10 :
	times = 0
	a = random.randint(-10,2)
	b = random.randint(-10,2)

	if fun1(a)*fun1(b) < 0 :
		t = t+1
		print("test",t,":",file = output)

		print("a =",a,file = output)
		print("b =",b,file = output)

		old_c = 0

		while 1 :
			times = times + 1
			fa = fun1(a)
			fb = fun1(b)
			c = (a*fb-b*fa)/(fb-fa)

			if fa*fun1(c) < 0 :
				b = c
				fa = fa / 2
			else :
				a = c
				fb = fb / 2

			if abs(old_c-c) < e :	
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			old_c = c
	
print("------------------------------------------",file = output)
print(file = output)

print("f(x) = exp(x*sin(x)) - x*cos(2*x) - 2.8",file = output)
print("range of x is [-5,5]",file = output)
print(file = output)

t = 0

while t != 10 :
	times = 0
	a = random.randint(-5,5)
	b = random.randint(-5,5)

	if fun2(a)*fun2(b) < 0 :
		t = t+1
		print("test",t,":",file = output)

		print("a =",a,file = output)
		print("b =",b,file = output)

		old_c = 0

		while 1 :
			times = times + 1
			fa = fun2(a)
			fb = fun2(b)
			c = (a*fb-b*fa)/(fb-fa)

			if fa*fun2(c) < 0 :
				b = c
				fa = fa / 2
			else :
				a = c
				fb = fb / 2

			if abs(old_c-c) < e :	
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			old_c = c

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

		old_c = 0

		while 1 :
			times = times + 1
			fa = fun3(a)
			fb = fun3(b)
			c = (a*fb-b*fa)/(fb-fa)

			if fa*fun3(c) < 0 :
				b = c
				fa = fa / 2
			else :
				a = c
				fb = fb / 2

			if abs(old_c-c) < e :	
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			old_c = c

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

		old_c = 0

		while 1 :
			times = times + 1
			fa = fun4(a)
			fb = fun4(b)
			c = (a*fb-b*fa)/(fb-fa)

			if fa*fun4(c) < 0 :
				b = c
				fa = fa / 2
			else :
				a = c
				fb = fb / 2

			if abs(old_c-c) < e :	
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			old_c = c