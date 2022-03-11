import numpy as np
class AI():
	def __init__(self):
		pass
	
	def evaulation(self, game):
		check_result, check_value = game.check()
		if check_result:
			if check_value == "X":
				return 1000
			elif check_value == "O":
				return -1000
		value = 0
		for row in range(3):
			x_counter = 0
			o_counter = 0
			for col in range(3):
				if game.value_at(row, col) == "X":
					x_counter += 1
				elif game.value_at(row, col) == "O":
					o_counter += 1
			if x_counter == 1 and o_counter == 0:
				value += 1
			elif x_counter == 2 and o_counter == 0:
				value += 10
			elif o_counter == 1 and x_counter == 0:
				value -= 1
			elif o_counter == 2 and x_counter == 0:
				value -= 10
		for col in range(3):
			x_counter = 0
			o_counter = 0
			for row in range(3):
				if game.value_at(row, col) == "X":
					x_counter += 1
				elif game.value_at(row, col) == "O":
					o_counter += 1
			if x_counter == 1 and o_counter == 0:
				value += 1
			elif x_counter == 2 and o_counter == 0:
				value += 10
			elif o_counter == 1 and x_counter == 0:
				value -= 1
			elif o_counter == 2 and x_counter == 0:
				value -= 10
		x_counter = 0
		o_counter = 0
		for diag in range(3):
			if game.value_at(diag,diag) == "X":
				x_counter += 1
			elif game.value_at(diag,diag) == "O":
				o_counter += 1
		if x_counter == 1 and o_counter == 0:
			value += 1
		elif x_counter == 2 and o_counter == 0:
			value += 10
		elif o_counter == 1 and x_counter == 0:
			value -= 1
		elif o_counter == 2 and x_counter == 0:
			value -= 10
			
		x_counter = 0
		o_counter = 0
		for diag in range(3):
			diag = 2 - diag
			if game.value_at(diag,diag) == "X":
				x_counter += 1
			elif game.value_at(diag,diag) == "O":
				o_counter += 1
		if x_counter == 1 and o_counter == 0:
			value += 1
		elif x_counter == 2 and o_counter == 0:
			value += 10
		elif o_counter == 1 and x_counter == 0:
			value -= 1
		elif o_counter == 2 and x_counter == 0:
			value -= 10
		return value
				
	
	def move(self, sign, game):
		legal_move = []
		ev_score = []
		if game.is_game_over():
			return
		for row in range(3):
			for col in range(3):
				board = game.get_board()
				a = row
				b = col
				if board[row][col] == ".":
					game.move(sign, row, col)
					new_board = game.get_board()
					temp_ev_score = []
					for new_row in range(3):
						for new_col in range(3):
							new_a = new_row
							new_b = new_col
							if new_board[new_row][new_col] == ".":
								if sign == "X":
									game.move("O", new_row, new_col)
								else:
									game.move("X", new_row, new_col)
								temp_ev = self.evaulation(game)
								temp_ev_score.append(temp_ev)
								game.undo_move_param(new_a, new_b)
					legal_move.append([a,b])
					ev_score.append(max(temp_ev_score))
					game.print_board()
					game.undo_move_param(a, b)
					
		move_d = legal_move[ev_score.index(min(ev_score))]
		game.move(sign, move_d[0], move_d[1])
		print(legal_move)
		print(ev_score)
		print("Played ", move_d)
		game.print_board()