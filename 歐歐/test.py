import random
import math
import numpy as np

out = open("out2.out", "w")

learning_rate = 1
e = 2.71828182846
hidden_unit = 10
p = np.ndarray(shape = (4,1) , dtype = float)
t = np.ndarray(shape = (3,1) , dtype = float)

w1 = np.ndarray(shape = (hidden_unit,4) , dtype = float)
b1 = np.ndarray(shape = (hidden_unit,1) , dtype = float)
a1 = np.ndarray(shape = (hidden_unit,1) , dtype = float)
er1 = np.ndarray(shape = (hidden_unit,1) , dtype = float)

w2 = np.ndarray(shape = (3,hidden_unit) , dtype = float) 
b2 = np.ndarray(shape = (3,1) , dtype = float)
a2 = np.ndarray(shape = (3,1) , dtype = float)
er2 = np.ndarray(shape = (3,1) , dtype = float)

print("Number of hidden neurons = ",hidden_unit,file = out)
print("Learning rates = ",learning_rate,file = out)

# three target
versicolor = np.array([[0.1],[0.9],[0.1]])
virginica = np.array([[0.1],[0.1],[0.9]])
setosa = np.array([[0.9],[0.1],[0.1]])

def target(t):
	if(t == 'versicolor'):
		return versicolor
	if(t == 'virginica'):
		return virginica
	if(t == 'setosa'):
		return setosa

for j in range(hidden_unit) :
	for i in range(3) :
		# w1[j][i] = random.random()
		w2[i][j] = random.random()
		b2[i] = random.random()
	b1[j] = random.random()

for i in range(hidden_unit):
	for j in range(4):
		w1[i][j] = random.random()

print("Initial weight1 = ",w1,file = out)
print("Initial weight2 = ",w2,file = out)
print("Initial bias1 = ",b1,file = out)
print("Initial bias2 = ",b2,file = out)
print("",file = out)

training = open(r'iris_training_data.txt') # read training file
text = []

# divide rows
for i in training :
	text.append(i)

epoch = 0
epoch_max = 100000

RMSE = 1.
RMSE_min = 1


# while (epoch < epoch_max and RMSE > 0.15):
# RMSE = 0.
# epoch += 1
# for t in text :
# 	t = t.strip('\n').split(" ")
# 	index = 0
# 	for n in t :
# 		if(index == 4) :
# 			t = target(n)
# 			break;
# 		n = float(n)
# 		p[index] = n
# 		index += 1
# 	# print("p =",p)
# 	# print("t =",t)

# 	# a1 & a2
# 	for i in range(hidden_unit):
# 		ah = w1[i].dot(p) + b1[i]
# 		ah = 1 / (1 + math.pow(e,-ah))
# 		a1[i] = ah
# 	# print("a1 = ",a1)

# 	for i in range(3) :
# 		ah = w2[i].dot(a1) + b2[i]
# 		ah = 1 / (1 + math.pow(e,-ah))
# 		a2[i] = ah
# 	# print("a2 = ",a2)

# 	# error & RMSE
# 	for j in range(hidden_unit):
# 		tmp = 0.
# 		for i in range(3) :
# 			tmp += w2[i][j] * er2[i]
# 		er1[j] = tmp * a1[j] * (1 - a1[j])
# 	# print("error1 =",er1)

# 	tmp = 0. 
# 	for i in range(3) :
# 		er2[i] = (t[i] - a2[i]) * a2[i] * (1 - a2[i])
# 		tmp += pow((t[i] - a2[i]),2)
# 	# print("error2 =",er2)

# 	#update
# 	for i in range(3) :
# 		for j in range(hidden_unit) :
# 			w1[j][i] = w1[j][i] + 2 * learning_rate * er1[j] * p[i]
# 			w2[i][j] = w2[i][j] + 2 * learning_rate * er2[i] * a1[j]
# 		b2[i] = b2[i] + 2 * learning_rate * er2[i]	
# 		b1[j] = b1[j] + 2 * learning_rate * er1[j]

# 	tmp /= 120
# 	RMSE += math.sqrt(tmp)

# 	if(RMSE < RMSE_min):
# 		RMSE_min = RMSE
# 		Last_w1 = w1
# 		Last_b1 = b1
# 		Last_b2 = b2
# 		Last_w2 = w2

# print("Last w1 : ",Last_w1,file = out)
# print("Last b1 : ",Last_b1,file = out)
# print("Last w2 : ",Last_w2,file = out)
# print("Last b2 : ",Last_b2,file = out)
# print("",file = out)
# print("Epoch =", epoch,file = out)

accuracies = 0

print("w1",w1)
print("w2",w2)
print("b1",b1)
print("b2",b2)

for t in text :
	t = t.strip('\n').split(" ")
	index = 0
	for n in t :
		if(index == 4) :
			# train_result.append(n)
			t = target(n)
			break;
		n = float(n)
		p[index] = n
		index += 1
	print("p",p)
	# a1 & a2
	for i in range(hidden_unit):
		ah = w1[i].dot(p) + b1[i]
		ah = 1 / (1 + math.pow(e,-ah))
		a1[i] = ah	
	for i in range(3) :
		ah = w2[i].dot(a1) + b2[i]
		ah = 1 / (1 + math.pow(e,-ah))
		a2[i] = ah
	# print("a2 = ",a2)	sss

	# # check
	# if((a == t).all()) :
	# 	accuracies += 1

	print("a2:",a2)
	# print("a2.max:",a2.max())

	for h in range(3):
		if(a2[h] == a2.max()):
			pos = h

	if(t[pos]==0.9):
		accuracies = accuracies + 1

print("accuracies-1",accuracies)
percent = accuracies / 120 * 100
print("training accuracies =",percent,file = out)

accuracies = 0
testing = open(r'iris_testing_data.txt') # read testing file
txt = []
# divide rows
for i in testing :
	txt.append(i)

for t in txt :
	t = t.strip('\n').split(" ")
	index = 0
	for n in t :
		if(index == 4) :
			# train_result.append(n)
			t = target(n)
			break;
		n = float(n)
		p[index] = n
		index += 1

	# a1 & a2
	for i in range(hidden_unit):
		ah = w1[i].dot(p) + b1[i]
		ah = 1 / (1 + math.pow(e,-ah))
		a1[i] = ah	
	# print("a1 = ",a1)
	for i in range(3) :
		ah = w2[i].dot(a1) + b2[i]
		ah = 1 / (1 + math.pow(e,-ah))
		a2[i] = ah
	# print("a2 = ",a2)

	for h in range(3):
		if(a2[h] == a2.max()):
			pos = h

	if(t[pos]==0.9):
		accuracies = accuracies + 1
print("accuracies-2",accuracies)
percent = accuracies / 30 * 100
print("testing  accuracies =",percent,file = out)