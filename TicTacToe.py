import time
import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

boardNumber = [0, 1, 2, 3, 4, 5, 6, 7, 8]

scores = {'X':10, 'O':-10, 'Tie':0}

player = None

def displayBoard():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])

def checkEmptyBoard():
	count = 0
	for i in board:
		if i == "-":
			count += 1
	if count == 9:
		return 0
	else:
		return 1

def checkWinStatus():
	res = checkWinner()
	if res == None:
		print("Game is On")
	else:
		if res == "X":
			print("Team X won")
			quit()
		elif res == "O":
			print("Team O won")
			quit()
		else:
			print("Tie")
			quit()


def checkWinner():
	winner = None

	#For Horizontal check
	horizontal = [0, 3, 6]
	for i in horizontal:
		if(board[i] == board[i+1] == board[i+2] != "-"):
			winner = board[i]

	#For Vertical Check
	for i in range(3):
		if(board[i] == board[i+3] == board[i+6] != "-"):
			winner = board[i]

	#For Diagonal Check
	if(board[0] == board[4] == board[8] != "-"):
		winner = board[0]
	if(board[2] == board[4] == board[6] != "-"):
		winner = board[2]

	#For Empty Checks
	openSpot = 0
	for i in range(9):
		if board[i] == "-":
			openSpot += 1


	if winner == None and openSpot == 0:
		return "Tie"
	else:
		return winner



 
def minimax(position, depth, maximizingPlayer):
	result = checkWinner()
	if result != None:
		return scores[result]

	if(maximizingPlayer):
		bestMove = float('-inf')
		for cspot in boardNumber:
			if board[cspot] == "-":
				board[cspot] = "X"
				move = minimax(board, depth+1, False)
				board[cspot] = "-"
				bestMove = max(move, bestMove)
		return bestMove
	else:
		bestMove = float('inf')
		for cspot in boardNumber:
				if board[cspot] == "-":
					board[cspot] = "O"
					move = minimax(board, depth+1, True)
					board[cspot] = "-"
					bestMove = min(move, bestMove)
		return bestMove





def playGame():
	global boardNumber
	if player == "X":
		print("Play your turn.\nChoose a spot where to place")
		spot = int(raw_input())
		board[spot-1] = "X"
		boardNumber.remove(spot-1)
		displayBoard()
		checkWinStatus()
		print("Wait for the computer to play his turn\nComputer thinking......")
		#time.sleep(10) 
		#cspot = random.choice(boardNumber)
		bestSpot = 0
		bestMove = float('inf')
		for cspot in boardNumber:
			if board[cspot] == "-":
				board[cspot] = "O"
				move = minimax(board, 0, True)
				board[cspot] = "-"
				if move < bestMove:
					bestMove = move
					bestSpot = cspot
		board[bestSpot] = "O"
		displayBoard()
		checkWinStatus()
		playGame()
		
	else:
		print("Wait for the computer to play his turn\nComputer thinking......")
		#time.sleep(10)
		#cspot = random.choice(boardNumber)
		if checkEmptyBoard() == 0:
			cspot = random.choice(boardNumber)
			board[cspot] = "X"
		else:
			bestSpot = 0
			bestMove = float('-inf')
			for cspot in boardNumber:
				if board[cspot] == "-":
					board[cspot] = "X"
					move = minimax(board, 0, False)
					board[cspot] = "-"
					if move > bestMove:
						bestMove = move
						bestSpot = cspot
			board[bestSpot] = "X"
		displayBoard()
		checkWinStatus()
		print("Play your turn.\nChoose a spot where to place")
		spot = int(raw_input())
		board[spot-1] = "O"
		boardNumber.remove(spot-1)
		displayBoard()
		checkWinStatus()
		playGame()




def startGame():
	global player
	print("Choose Your Team: X or O")
	player = raw_input()
	if player == "X":
		computer = "O"
	else:
		computer = "X"
	displayBoard()
	print("You: "+player+" and Opponent: "+computer)
	playGame()

startGame()

