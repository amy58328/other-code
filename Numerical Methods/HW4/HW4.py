import numpy as np

x = []
y = []
xn = []
yn = []
A = []
B = []
def readdata():
	file = open('data.txt', 'r')
	for i in file.readlines():
		a,b = i.split()
		x.append(float(a))
		y.append(float(b))
	# xn.append(len(x))

def find_xn(t):
	s = 0
	for i in x:
		s += pow(i,t)
	xn.append(s)
def find_yn(t):
	s = 0

	for i in range(0,len(y)):
		tt = y[i] * pow(x[i],t)
		# print(tt)
		s += tt
	yn.append(s)


def Least_Square(t):
	

readdata()
for i in range(0,50):
	find_xn(i)
	find_yn(i)
Least_Square(2)