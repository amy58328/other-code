import random

while True:
	print("enter the number that you want to test\n1. ch1\n2. ch2\n3. ch4\n4. ch7\n5. ch8\n6. all\n7. end the test.\n")
	a = input("enter number : ")

	if(a == '7'):
		break

	file = open("ch1.txt","r",encoding='utf-8')
	all = 23
	if(a == '1'):
		file = open("ch1.txt","r",encoding='utf-8')
		all = 23
	elif(a == '2'):
		file = open("ch2.txt","r",encoding='utf-8')
		all = 17
	elif(a == '3'):
		file = open("ch4.txt","r",encoding='utf-8')
		all = 11
	elif(a == '4'):
		file = open("ch7.txt","r",encoding='utf-8')
		all = 17
	elif(a == '5'):
		file = open("ch8.txt","r",encoding='utf-8')
		all = 16
	elif(a == '6'):
		file = open("sentence.txt","r",encoding='utf-8')
		all = 84

	print("the number of questions is ",all,end="")
	n = input(", enter the number of questions that you want to test : ")

	n = int(n)
	li = [i for i in range(all)]

	order = random.sample(li,n)

	lines = file.readlines()
	sentence = []

	for i in lines:
		a = i.split(".")
		sentence.append(a)

	order = random.sample(li,n)

	score = 0
	total = 0
	index = 1
	for i in order:
		print(index,end="、")
		index += 1
		print(sentence[i][0])

		for j in range(1,len(sentence[i])-1):
			print(j,":")
			word = input()
			total += 1
			if(word == sentence[i][j]):

				score += 1
			else:
				print(sentence[i][j])
				word = input("write again:")
				if(word != sentence[i][j]):
					print("still wrong")

		print()
	print("scor = %d/%d"%(score,total))
