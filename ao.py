# TO DISPLAY THE MAIN TIC TAC TOE BOARD OF TTHE GAME

def display_board(board):
	print('\n' * 100)
	print('                     ' + board[1] + '  |  ' +board[2] + '  |  ' + board[3] + '     ')
	print('                     ' + "-"      + '  |  ' +'-'      + '  |  ' + "-"      + '     ')
	print('                     ' + board[4] + '  |  ' +board[5] + '  |  ' + board[6] + '     ')
	print('                     ' + "-"      + '  |  ' +'-'      + '  |  ' + "-"      + '     ')
	print('                     ' + board[7] + '  |  ' +board[8] + '  |  ' + board[9] + '     ')

# TO TAKE INPUT FROM BOTH THE PLAYERS OF WHAT SYMBOL EACH ONE WANTS TO TAKE

def player_input():
	player_1 = input('Player 1, please choose your symbol between X or O: ')
	while player_1 != 'X' and player_1 != 'O':
		player_1 = input('Player 1, please choose your symbol between X or O: ')
	else:
		if player_1 == 'X':
			player_2 = 'O'
		else:
			player_2 = 'X'
	return (player_1,player_2)

# FUNCTION TO COMBINE DISPLAY BOARD, MARKER AND DESIRED POSTION

def place_marker(board, marker, postion):
	board[postion] = marker

# FUNCTION TO CHECK IF THAT MARK HAS WON THE GAME

def win_check(board , marker):
	return (board[1] == marker and board[2] == marker and board[3] == marker) or (board[4] == marker and board[5] == marker and board[6] == marker) or (board[7] == marker and board[8] == marker and board[9] == marker) or (board[1] == marker and board[4] == marker and board[7] == marker) or(board[2] == marker and board[5] == marker and board[8] == marker) or (board[3] == marker and board[6] == marker and board[9] == marker) or(board[1] == marker and board[5] == marker and board[9] == marker) or (board[3] == marker and board[5] == marker and board[7] == marker) 

# TO RANDOMLY DECIDE WHICH PLAYER WILL GO FIRST

import random

def choose_first():
	if random.randint(0,1) == 0:
		return "Player 2"
	else:
		return "Player 1"

# TO CHECK IF THE SPACE IS EMPTY AT A PARTICULAR INDEX I.E RETURNS TRUE FOR AN EMPTY SPACE

def space_check(board , postion):
	return board[postion] == ' '

# TO CHECK IF THE BOARD IS FULL OR NOT: TRUE FOR FULL AND FALSE FOR EMPTY

def full_board_check(board):
	for i in range(0,len(board)):
		if space_check(board,i):		# RETURNS FALSE IF ANY VALUE IS FOUND AT THE PARTICULAR INDEX
			return False 
	return True

# TO ASK PLAYERS NEXT POSITON AND USING FUNCTION SPCAE CHECK TO CHECK THE FREE SPACE

def player_choice(board):
	choice = 0
	while choice not in [1,2,3,4,5,6,7,8,9] or not space_check(board, choice):
		choice = int(input("Enter your next postion (1-9): "))
	return choice

# TO ASK THE PLAYERS WHEATHER THEY WANT TO PLAY THE GAME AGAIN

def replay():
	choice = input("Do you want to play the again ? ")
	if choice.lower() == 'yes':
		return True 
	else:
		return False


print("     Welcome to the Tic Tac Toe Game! ")
while True:
	board = [' '] * 11
	Player_1, Player_2 = player_input()
	turn = choose_first()
	print(turn + " will go first ")

	play_game = input("Are you ready to play ? ")

	if play_game.lower() == 'yes':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == 'Player 1':

			#PLAYER 1 TURN
			
			display_board(board)
			position = player_choice(board)
			place_marker(board, Player_1, position)

			if win_check(board, Player_1):
				display_board(board)
				print("Congratulations you've won the game!! Player 1!")
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print("The game is a draw!! ")
					break
				else:
					turn = 'Player 2'
		else:

			#PLAYER 2 TURN
			display_board(board)
			postion = player_choice(board)
			place_marker(board, Player_2, postion)
			if win_check(board, Player_2):
				display_board(board)
				print("Congratulations you've won the game !! Player 2")
				game_on = False
			else:

				if full_board_check(board):
					display_board(board)
					print("The game is draw ! ")
					break
				else:
					turn = 'Player 1'

	if not replay():
		break