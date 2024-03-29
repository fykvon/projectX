from django.db.models import Sum, Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Player, Team


class PlayerServices:
    """Service for model Player"""
    @receiver(post_save, sender=Player)
    def update_team_goals(sender, instance, **kwargs):
        """Method count team goals"""
        team = instance.team
        players = Player.objects.filter(team=team)
        total_goals = players.aggregate(total_goals=Sum('goals'))['total_goals']
        team.goals = total_goals
        team.save()

    @receiver(post_save, sender=Player)
    def update_team_missed_goals(sender, instance, **kwargs):
        """Method count team missed goals"""
        team = instance.team
        players = Player.objects.filter(team=team)
        missed_goals = players.aggregate(total_missed_goals=Sum('missed_goals'))['total_missed_goals']
        team.missed_goals = missed_goals
        team.save()

    @receiver(post_save, sender=Player)
    def update_team_yellow_cards(sender, instance, **kwargs):
        """Method count team yellow cards"""
        team = instance.team
        players = Player.objects.filter(team=team)
        yellow_cards = players.aggregate(total_yellow_cards=Sum('yellow_cards'))['total_yellow_cards']
        team.yellow_cards = yellow_cards
        team.save()

    @receiver(post_save, sender=Player)
    def update_team_red_cards(sender, instance, **kwargs):
        """Method count team red cards"""
        team = instance.team
        players = Player.objects.filter(team=team)
        red_cards = players.aggregate(total_red_cards=Sum('red_cards'))['total_red_cards']
        team.red_cards = red_cards
        team.save()

    @staticmethod
    def best_strikers(player):
        """Method return Queryset with 10 players with goals more then 0"""
        best_strikers = player.filter(goals__gt=0).order_by('-goals')[:10]
        return best_strikers

    @staticmethod
    def best_assists(player):
        """Method return Queryset with 10 players with assists more then 0"""
        best_assists = player.filter(assists__gt=0).order_by('-assists')[:10]
        return best_assists

    @staticmethod
    def most_red_cards(player):
        """Method return Queryset with 10 players with red_cards more then 0"""
        most_red_cards = player.filter(red_cards__gt=0).order_by('-red_cards')[:10]
        return most_red_cards

    @staticmethod
    def most_yellow_cards(player):
        """Method return Queryset with 10 players with yellow_cards more then 0"""
        yellow_cards = player.filter(yellow_cards__gt=0).order_by('-yellow_cards')[:10]
        return yellow_cards


class TeamServices:

    @staticmethod
    def main_service():
        """Method count and update team stats"""
        teams = Team.objects.all()
        for team in teams:
            delta = team.goals - team.missed_goals
            team.delta_goals = delta
            points = (team.win * 3) + team.draw
            team.points = points
            games = team.win + team.draw + team.lose
            team.games = games
            team.save()
