import random


while True:
	file = open("file.txt","r",encoding='utf-8')

	lines = file.readlines()
	elist = []
	clist = []
	all = 0
	for i in lines:
		# print(i)
		all += 1
		a,b,c = i.split(".")
		elist.append(a)
		clist.append(b)

	print("the number of questions is ",all,end="")
	n = input(", enter the number of questions that you want to test :(-1 for break) ")
	n = int(n)

	if(n == -1):
		break

	li = [i for i in range(all)]

	# order = random.sample(li,n)





	#  print chinese enter english
	# order = random.sample(li,n)

	score = 0
	index = 1
	for i in range(0,len(elist)):
		print(index," : ",clist[i])
		index+=1
		message = input()
		if(message==elist[i]):
			score+=1
			continue
		else:
			print(elist[i])
			message = input("再輸入一遍")
			if(message!=elist[i]):
				print("還是錯的")

	print("\n score = ",score,"/",n)		


	#  print english enter chinese

	# order = random.sample(li,n)
	score = 0
	index = 1
	for i in range(0,len(clist)):
		print(index," : ",elist[i]) 
		index += 1
		message = input()
		if(message==clist[i]):
			score+=1
			continue
		else:
			print(clist[i])
			message = input("再輸入一遍")

	print("\n score = ",score,"/",n)
