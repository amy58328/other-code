import random


file = open("file.txt","r",encoding='utf-8')


all = 89
n = 20
li = [i for i in range(all)]

order = random.sample(li,n)

lines = file.readlines()
elist = []
clist = []

for i in lines:
	# print(i)
	a,b = i.split()
	elist.append(a)
	clist.append(b)

order = random.sample(li,n)

score = 0
index = 1
for i in order:
	print(index," : ",clist[i])
	index+=1
	message = input()
	if(message==elist[i]):
		score+=1
		continue
	else:
		print(elist[i])

print("\n score = ",score,"/",n)		

order = random.sample(li,n)
score = 0
index = 1
for i in order:
	print(index," : ",elist[i]) 
	message = input()
	if(message==clist[i]):
		score+=1
		continue
	else:
		print(clist[i])

print("\n score = ",score,"/",n)
