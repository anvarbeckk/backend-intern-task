from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='tournament_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='tournament_user_set', blank=True)

class Player(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    rating = models.IntegerField()
    country = models.CharField(max_length=200)


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(Player)


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    round_number = models.IntegerField()
    player1 = models.ForeignKey(Player, related_name='player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='player2', on_delete=models.CASCADE)
    result = models.CharField(max_length=10)
    