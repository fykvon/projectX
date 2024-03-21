from django.shortcuts import render
from django.views.generic import (CreateView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView,
                                  )
from rest_framework import viewsets

from .services import PlayerServices, TeamServices
from .models import Player, Team, Division
from .serializer import PlayerSerializer


class CreatePlayerView(CreateView):
    model = Player
    fields = ['role', 'f_name', 's_name', 'team', 'image']
    template_name = 'general_api/create_player.html'


class UpdatePlayerView(UpdateView):
    pass


class DeletePlayerView(DeleteView):
    pass


class DetailPlayerView(DetailView):
    model = Player
    template_name = 'general_api/detail_player.html'

    def get(self, request, *args, **kwargs):
        players = Player.objects.all()
        return render(request, self.template_name, context={'players': players})


class PlayerViewSet(viewsets.ModelViewSet):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class DivisionView(DetailView):
    """
    Divisions view. In this view separated teams on divisions
    """
    template_name = 'general_api/divisions/division.html'

    def get(self, request, *args, **kwargs):
        divisions_queryset = Division.objects.all()
        divisions = {}
        for division in divisions_queryset:
            teams = Team.objects.filter(division__name=division.name).order_by('-points')
            divisions[division] = teams
        TeamServices.main_service()
        return render(request, self.template_name,
                      context={'divisions': divisions})


class DivisionDetailView(DetailView):
    """
    This view contains information about teams in division
    """
    model = Division
    template_name = 'general_api/divisions/division_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        division = self.model.objects.get(id=self.kwargs['pk'])
        teams = Team.objects.filter(division=division.pk).order_by('-points')
        player = Player.objects.filter(team__division__pk=division.pk)
        forwards = PlayerServices.best_strikers(player=player)
        red_cards = PlayerServices.most_red_cards(player=player)
        yellow_cards = PlayerServices.most_yellow_cards(player=player)
        assists = PlayerServices.best_assists(player=player)
        TeamServices.main_service()
        context.update({'teams': teams, 'forwards': forwards, 'red_cards': red_cards, 'yellow_cards': yellow_cards,
                        'assists': assists, })
        return context


class PlayerDetailView(DetailView):
    """Player Detail view"""
    model = Player
    template_name = 'general_api/players/player_detail.html'

    def get(self, request, *args, **kwargs):
        player = self.model.objects.get(pk=self.kwargs['pk'])
        division = player.team.division
        return render(request, self.template_name, context={'player': player, 'division': division})


class TeamDetailView(DetailView):
    """Team Detail view"""
    model = Team
    template_name = 'general_api/teams/team_detail.html'

    def get(self, request, *args, **kwargs):
        team = self.model.objects.get(slug=self.kwargs['slug'])
        players = Player.objects.filter(team__slug=team.slug)
        return render(request, self.template_name, context={'team': team, 'players': players})
