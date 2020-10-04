import numpy as np
import math
import matplotlib.pyplot as plt

x = []
y = []
xn = []
yn = []
mini_sigma = 20
ans_time = []
funal_array = []
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
	A = []
	b = []
	for i in range(0,t):
		temp = []
		for j in range(i,i+t):
			temp.append(xn[j])
		A.append(temp)
		b.append(yn[i])

	a  = np.linalg.solve(A,b)
	return a 


def f(X,t,a):
	Sum = 0
	aa = []
	for i in range(0,t):
		Sum += a[i] * (X ** i)
	return Sum



readdata()
for i in range(0,100):
	find_xn(i)
	find_yn(i)
for i in range(1,45):
	a = Least_Square(i)
	Sum = 0
	aa = []
	for j in range(0,len(x)):
		temp = f(x[j],i,a)
		Sum += math.pow((y[j]- temp),2)
		aa.append(temp)
	sigma = math.sqrt(Sum/(len(x) - i))

	# if sigma <= mini_sigma:
	if i == 31:
		mini_sigma = sigma
		ans_time = i;
		finall_array = aa

# print(ans_time)
# print(finall_array)

title = "P" + str(ans_time-1) + "(x)" + " Sigma = " + str(mini_sigma)
plt.title(title)
plt.plot(x,y,'red',label = "raw_data")
plt.plot(x,finall_array,'blue',label = "Prediction_line")
plt.legend()
plt.show()