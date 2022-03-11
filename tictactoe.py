class Board():
	def __init__(self):
		self.last_row = 0
		self.last_col = 0
		self.board = [
			[".",".","."],
			[".",".","."],
			[".",".","."]
		]
	def check(self):
		for row in range(3):
			if self.board[row][0] != "." and self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2]:
				return True,self.board[row][0]
		for col in range(3):
			if self.board[0][col] != "." and self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col]:
				return True,self.board[0][col]
		if self.board[0][0] != "." and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
			return True, self.board[0][0]
		if self.board[0][2] != "." and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
			return True, self.board[0][2]
		return False, None
	
	def is_game_over(self):
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == ".":
					return False
		return True
	
	def move(self,sign,row,col):
		if self.board[row][col] == ".":
			self.board[row][col] = sign
		else:
			print("Illegal Move")
			return -1
		self.last_row = row
		self.last_col = col
		
	
	def undo_move(self):
		self.board[self.last_row][self.last_col] = "."
		
	def undo_move_param(self,row,col):
		self.board[row][col] = "."
	
	def print_board(self):
		print("\n")
		for row in range(3):
			print(self.board[row][0] + "\t" + self.board[row][1] + "\t" + self.board[row][2])
		

	def get_board(self):
		return self.board
	
	def value_at(self, row, col):
		return self.board[row][col]