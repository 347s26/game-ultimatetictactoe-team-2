from django.db import models
from django.urls import reverse

# Create your models here.


class Game(models.Model):
    """Model representing the game"""
    id = models.IntegerField
    player_x_id = models.ManyToManyField("User", related_name = "player_x_game")
    player_o_id = models.ManyToManyField("User", related_name = "player_o_game")
    board = models.JSONField
    turn = models.BooleanField  # True for X, False for O
    game_active = models.BooleanField
    mini_board_winners = models.JSONField
    current_board = models.IntegerField
    next_board = models.IntegerField


class User(models.Model):
    id = models.IntegerField
