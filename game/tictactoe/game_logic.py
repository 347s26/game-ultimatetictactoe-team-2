import json
class GameLogic:

	def __init__(self, obj, mini_board, cell, player, game_id):
		self.obj = obj
		self.mini_board = mini_board
		self.cell = cell
		self.player = player
		self.game_id = game_id
		self.mini_board_winners = None  # optional: track mini-board winners

	def test(self):
		if self.obj.board[self.mini_board][self.cell] == "":
			self.obj.board[self.mini_board][self.cell] = "X"
			self.obj.save()
			return True
		else: return False

