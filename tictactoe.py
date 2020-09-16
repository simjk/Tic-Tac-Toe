
board = ["-", "-", "-",
		"-", "-", "-",
		"-", "-", "-"]

#global variable
winner = None
game_ongoing = True

current_player = "X"


def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])
	print("\n")


def play_game():
	#players 1 and 2
	player_1, player_2 = players_name()

	#initial empty board
	display_board()

	while game_ongoing:
		handle_turn(current_player, player_1, player_2)
		
		#Check whether the game ended
		check_game()

		#Switch turn
		flip_player()

	#Game ended
	if winner == "X":
		print(player_1 + " won.")
	elif winner == "O":
		print(player_2 + " won.")
	else:
		print("Tie.")

def players_name():
	player_1 = input("Choose a name for Player 1: ")
	player_2 = input("Choose a name for Player 2: ")
	return player_1, player_2

def handle_turn(player, player_1, player_2):

	if player == "X":
		print(player_1 + "'s turn.")
	elif player == "O":
		print(player_2 + "'s turn.")
	position = input("Choose a position from 1-9: ")

	valid = False
	while not valid:
		#Verify the position chosen is within the board
		while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			position = input("Choose a position from 1-9: ")

		position = int(position) - 1

		if board[position] == "-":
			valid = True
		else:
			print("The board is chosen. Try again.")

	board[position] = player
	display_board()


def check_game():
	check_for_winner()
	check_if_tie()


def check_for_winner():
	#set global variable
	global winner
	#check row
	#check columns
	#check diagonals
	row_winner = check_rows()
	column_winner = check_columns()
	diagonal_winner = check_diagonals()

	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else:
		#there is no winners, it is a tie
		winner = None
	return

def check_rows():
	#Check the status of the game
	global game_ongoing
	row_1 = board[0] == board[1] == board[2] != "-"
	row_2 = board[3] == board[4] == board[5] != "-"
	row_3 = board[6] == board[7] == board[8] != "-"

	if row_1 or row_2 or row_3:
		game_ongoing = False
	if row_1:
		return board[0]
	elif row_2:
		return board[3]
	elif row_3:
		return board[6]
	else:
		return None

def check_columns():
	#Check the status of the game
	global game_ongoing
	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"

	if column_1 or column_2 or column_3:
		game_ongoing = False
	if column_1:
		return board[0]
	elif column_2:
		return board[1]
	elif column_3:
		return board[2]
	else:
		return None

def check_diagonals():
	#Check the status of the game
	global game_ongoing
	diagonals_1 = board[0] == board[4] == board[8] != "-"
	diagonals_2 = board[2] == board[4] == board[6] != "-"

	if diagonals_1 or diagonals_2:
		game_ongoing = False
	if diagonals_1:
		return board[0]
	elif diagonals_2:
		return board[2]
	else:
		return None

def check_if_tie():
	global game_ongoing
	if "-" not in board:
		game_ongoing = False
		return True
	else:
		return False


def flip_player():
	global current_player
	if current_player == "X":
		current_player = "O"
	elif current_player == "O":
		current_player = "X"
	return

#Start
play_game()