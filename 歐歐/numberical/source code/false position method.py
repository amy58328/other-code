import numpy as np
import random
import math

output = open("false position method.out", "w")

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

		old_c = 0

		while 1 :
			times = times + 1
			c = (a*fun1(b)-b*fun1(a))/(fun1(b)-fun1(a))

			if fun1(a)*fun1(c) < 0 :
				b = c
			else :
				a = c

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

while(t != 10) :
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
			c = (a*fun2(b)-b*fun2(a))/(fun2(b)-fun2(a))

			if fun2(a)*fun2(c) < 0 :
				b = c
			else :
				a = c

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
			c = (a*fun3(b)-b*fun3(a))/(fun3(b)-fun3(a))

			if fun3(a)*fun3(c) < 0 :
				b = c
			else :
				a = c

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
			c = (a*fun4(b)-b*fun4(a))/(fun4(b)-fun4(a))

			if fun4(a)*fun4(c) < 0 :
				b = c
			else :
				a = c

			if abs(old_c-c) < e :	
				print("times =",times,"=>",c,file = output)
				print(file = output)
				break

			old_c = c