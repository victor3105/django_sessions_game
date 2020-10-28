from django.db import models


class Player(models.Model):
    def __str__(self):
        return f'Player {id}'


class Game(models.Model):
    is_finished = models.BooleanField()
    players = models.ManyToManyField(Player, through='PlayerGameInfo', blank=True, null=True)

    def __str__(self):
        return f'Game {id}'


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
