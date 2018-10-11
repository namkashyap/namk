a=[1,2,3,4,5,6,7,8,9]
def printBoard():
	print(a[0],'|',a[1],'|',a[2])
	print("------------------")
	print(a[3],'|',a[4],'|',a[5])
	print("------------------")
	print(a[6],'|',a[7],'|',a[8])
	print("-------------------")

playeroneturn = True

while True:
	printBoard()
	p = int(input("choose your place>>"))
	if(p in a):
		if playeroneturn:
			#p = input("choose your place, Player 1>>")
			print("player1 chose:",p)
			a[int(p)-1] = 'X'
			playeroneturn = not playeroneturn
		else:
			#p = input("choose your place, Player 2>>")
			print("player2 chose:",p)
			a[int(p)-1] = 'O'
			playeroneturn = not playeroneturn				
		
		#check winning conditons:
		for i in (0,3,6):
			if(a[i]==a[i+1] and a[i]==a[i+2]):
				if a[i]=='X':
					print("player 1 wins!")
					exit()
					print("player 2 wins!")
					exit()
		for i in range(3):
			if(a[i]==a[i+3] and a[i]==a[i+6]):
				if a[i]=='X':
					print("player 1 wins!")
					exit()
					print("player 1 wins!")
					exit()
		if()				
		if()