from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.


class Game(models.Model):
    """Model representing the game"""
    player_x = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="player_x_games",
        on_delete=models.CASCADE,
        default=None
    )
    player_o = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="player_o_games",
        on_delete=models.CASCADE,
        default=None
    )
    
    board = models.JSONField(default=list)  # Main 9x9 board state, e.g., ["", "", "", ...]
    turn = models.BooleanField(default=True)  # True = X, False = O
    game_active = models.BooleanField(default=True)
    mini_board_winners = models.JSONField(default=list)  # Track 3x3 mini-board winners
    current_board = models.IntegerField(default=0)  # Which mini-board is active
    next_board = models.IntegerField(default=-1)    # Which mini-board the next player must play in (-1 = any)
    
    def __str__(self):
        return f"Game {self.id} - X:{self.player_x} O:{self.player_o}"
