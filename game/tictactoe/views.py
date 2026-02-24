from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from tictactoe.game_logic import GameLogic
from tictactoe.models import Game
# Create your views here.
def index(request):
    return render(request, 'index.html', {"sam":"sam"})
    

@csrf_exempt
def game(request):
	if request.method == 'POST':
		data 		= json.loads(request.body) 
		mini_board 	= int(data.get('miniBoard'))
		cell 		= int(data.get('cell'))
		game_id 	= int(data.get('gameId'))
		player		= bool(data.get('player'))

		try:
			game_obj = Game.objects.get(id=game_id)
		except Game.DoesNotExist:
			game_obj = None

		game_logic = GameLogic(game_obj, mini_board, cell, player, game_id)
             
		if game_logic.test():
			return JsonResponse({'moveAllowed': True, 'miniBoard': mini_board, 'cell': cell})
		else: return JsonResponse({'moveAllowed': False, 'miniBoard': mini_board, 'cell': cell})
	return JsonResponse({'error': 'invalid request'}, status=400)
    