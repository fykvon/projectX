from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Player


@receiver(post_save, sender=Player)
def update_team_goals(sender, instance, **kwargs):
    team = instance.team
    players = Player.objects.filter(team=team)
    total_goals = players.aggregate(total_goals=Sum('goals'))['total_goals']
    team.goals = total_goals
    team.save()

# TODO: count missed goals (explain how you can do it)
# @receiver(post_save, sender=Player)
# def update_team_missed_goals(sender, instance, **kwargs):
#     team = instance.team
#     players = Player.objects.filter(team=team)
#     missed_goals = players.aggregate(total_goals=Sum('missed_goals'))['missed_goals']
#     team.missed_goals = missed_goals
#     team.save()


@receiver(post_save, sender=Player)
def update_team_yellow_cards(sender, instance, **kwargs):
    team = instance.team
    players = Player.objects.filter(team=team)
    yellow_cards = players.aggregate(total_goals=Sum('yellow_cards'))['yellow_cards']
    team.goals = yellow_cards
    team.save()


@receiver(post_save, sender=Player)
def update_team_red_cards(sender, instance, **kwargs):
    team = instance.team
    players = Player.objects.filter(team=team)
    red_cards = players.aggregate(total_goals=Sum('red_cards'))['red_cards']
    team.goals = red_cards
    team.save()

