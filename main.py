import tictactoe as tt
import tictactoe_ai as tt_ai

game = tt.Board()
ai = tt_ai.AI()

while True:
	check_result, check_value = game.check()
	if check_result:
		print("Game Over. Winner: ", check_value)
		break
	elif game.is_game_over() == True:
		print("Draw")
		break
	user_row = int(input("Row: "))
	user_col = int(input("Column: "))
	move_state = game.move("X", user_row, user_col)
	while move_state is not None and move_state == -1:
		user_row = int(input("Row: "))
		user_col = int(input("Column: "))
		move_state = game.move("X", user_row, user_col)
	game.print_board()
	ai.move("O", game)