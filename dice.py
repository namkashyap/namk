DICE-
import random
while True:
	n=input("enter q to quit and r to roll the dice")

	if(n=='q'):
		print("bye!")
		exit()
	elif(n=='r'):
		r=random.randint(1,7)
		print(r)
		exit()

