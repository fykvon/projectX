from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Player, Team


class PlayerServices:
    @receiver(post_save, sender=Player)
    def update_team_goals(sender, instance, **kwargs):
        team = instance.team
        players = Player.objects.filter(team=team)
        total_goals = players.aggregate(total_goals=Sum('goals'))['total_goals']
        team.goals = total_goals
        team.save()

    @receiver(post_save, sender=Player)
    def update_team_missed_goals(sender, instance, **kwargs):
        team = instance.team
        players = Player.objects.filter(team=team)
        missed_goals = players.aggregate(total_missed_goals=Sum('missed_goals'))['missed_goals']
        team.missed_goals = missed_goals
        team.save()

    @receiver(post_save, sender=Player)
    def update_team_yellow_cards(sender, instance, **kwargs):
        team = instance.team
        players = Player.objects.filter(team=team)
        yellow_cards = players.aggregate(total_yellow_cards=Sum('yellow_cards'))['total_yellow_cards']
        team.yellow_cards = yellow_cards
        team.save()

    @receiver(post_save, sender=Player)
    def update_team_red_cards(sender, instance, **kwargs):
        team = instance.team
        players = Player.objects.filter(team=team)
        red_cards = players.aggregate(total_red_cards=Sum('red_cards'))['total_red_cards']
        team.red_cards = red_cards
        team.save()

    @staticmethod
    def best_strikers():
        best_strikers = Player.objects.order_by('-goals')[:10]
        return best_strikers


# class TeamServices:
#
#     @receiver(post_save, sender=Team)
#     def delta_goals_count(sender, instance, **kwargs):
#         team = instance
#         delta = team.goals - team.missed_goals
#         team.delta_goals = delta
#         points = (team.win * 3) + team.draw
#         team.points = points
#         games = team.win + team.draw + team.lose
#         team.games = games
#         team.save()
