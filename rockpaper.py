import random
print("welcome to rock paper scissors")
r={1:'r',2:'p',3:'s'}
while True:
	comp=r[random.randint(1,3)]
	p=input("enter r/p/s or q to quit")
	if p=='q':
		print("bye")
		exit()	
	elif (p=='comp'):
		print("its a tie")
	elif(p=='r'):
		if(comp=='s'):
				print("you win")
		else:
				print("comp wins")
	elif(p=='p'):
		if(comp=='r'):
				print("you win")
		else:
				print("comp wins")
	elif(p=='s'):
		if(comp=='p'):
				print("you win")
		else:
				print("comp wins")
