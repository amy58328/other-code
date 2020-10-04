import random

file = open("ch1.txt","r",encoding='utf-8')
all = -1
sentence = []

def numbers():
	all = 0
	lines = file.readlines()
	sentence.clear()
	for i in lines:
		all += 1
		a = i.split(".")
		sentence.append(a)
	return all 


while True:
	print("enter the number that you want to test\n1. ch1\n2. ch2\n3. ch4\n4. ch7\n5. ch8\n6. all\n7. wrong.\n8. end the test.\n")
	a = input("enter number : ")

	if(a == '8'):
		break

	if(a == '1'):
		file = open("ch1.txt","r",encoding='utf-8')
	elif(a == '2'):
		file = open("ch2.txt","r",encoding='utf-8')
	elif(a == '3'):
		file = open("ch4.txt","r",encoding='utf-8')
	elif(a == '4'):
		file = open("ch7.txt","r",encoding='utf-8')
	elif(a == '5'):
		file = open("ch8.txt","r",encoding='utf-8')
	elif(a == '6'):
		file = open("all.txt","r",encoding='utf-8')
	elif(a == '7'):
		file = open("wrong.txt","r",encoding='utf-8')

	all = numbers()

	print("the number of questions is ",all,end="")
	n = input(", enter the number of questions that you want to test : ")

	n = int(n)
	li = [i for i in range(all)]

	order = random.sample(li,n)

	score = 0
	total = 0
	index = 1
	for i in order:
		print(index,end="、")
		index += 1
		print(sentence[i][0])

		for j in range(1,len(sentence[i])-1,2):
			print(int(j/2+1),end = ":")
			word = input("英文:  ")
			total += 1
			cor = 0
			if(word == sentence[i][j]):
				cor += 1
			else:
				print("正確答案是 : ",sentence[i][j])
				word = input("再輸入一次: ")
				while(word != sentence[i][j]):
					print("still wrong")
					word = input("再輸入一次: ")

			word = input("中文:  ")
			if(word == sentence[i][j+1]):
				cor += 1
			else:
				print("正確答案是 : ",sentence[i][j+1])
				word = input("再輸入一次: ")
				while(word != sentence[i][j+1]):
					print("still wrong")
					word = input("再輸入一次: ")

			if(cor == 2):
				score += 1
		print()
	print("scor = %d/%d"%(score,total))
