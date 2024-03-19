from django.db import models
from django.urls import reverse


class Division(models.Model):
    """
    Model representing a Division
    """

    name = models.CharField(max_length=100, verbose_name='division name')
    year = models.CharField(max_length=4, verbose_name='division year')

    def get_absolute_url(self):
        return reverse("general_api:division_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Team(models.Model):
    """
    Model representing a Team
    """

    name = models.CharField(max_length=40, unique=True, verbose_name='Team name')
    slug = models.CharField(auto_created=True, max_length=25, verbose_name='Team slug')
    division = models.ForeignKey(Division, on_delete=models.PROTECT, verbose_name='Team division')
    win = models.IntegerField(default=0, verbose_name=' Total winning')
    lose = models.IntegerField(default=0, verbose_name='Total losing')
    draw = models.IntegerField(default=0, verbose_name='Total drawing')
    goals = models.IntegerField(default=0, verbose_name='Total team goals')
    missed_goals = models.IntegerField(default=0, verbose_name='Total team missed goals')
    yellow_cards = models.IntegerField(default=0, verbose_name='Total team yellow cards')
    red_cards = models.IntegerField(default=0, verbose_name='Total team red cards')
    team_photo = models.ImageField(upload_to='static/team_photo/', default='static/none_image_team_photo.jpg/')
    team_logo = models.ImageField(upload_to='static/team_logo/', default='static/none_image_team_logo.jpg/')
    delta_goals = models.IntegerField(default=0, verbose_name='Delta goals')
    points = models.IntegerField(default=0, verbose_name='Points')
    games = models.IntegerField(default=0, verbose_name='Games')

    def __str__(self):
        return f'{self.name}'


class Player(models.Model):
    """
    Model representing a player
    """

    ROLE = [('GK', 'Goalkeeper'),
            ('PL', 'Player'),
            ('CH', 'COACH')]

    role = models.CharField(max_length=30, choices=ROLE, blank=False, null=False, verbose_name='role on field')
    f_name = models.CharField(max_length=30, blank=False, null=False, verbose_name='First name')
    s_name = models.CharField(max_length=30, blank=False, null=False, verbose_name='Second name')
    year_born = models.IntegerField(blank=True, null=True, verbose_name='Year born')
    team = models.ForeignKey(Team, on_delete=models.PROTECT, default='Without teams', verbose_name='Team')
    image = models.ImageField(upload_to=f'static/player/photo/')
    goals = models.IntegerField(default=0, verbose_name='Total player goals')
    assists = models.IntegerField(default=0, verbose_name='Total player assists')
    yellow_cards = models.IntegerField(default=0, verbose_name='Total player yellow cards')
    red_cards = models.IntegerField(default=0, verbose_name='Total player red cards')
    games = models.IntegerField(default=0, verbose_name='Played_games')
    is_active = models.BooleanField(default=True, verbose_name='Active player')
    missed_goals = models.IntegerField(default=0, verbose_name='Missed goals')

    def __str__(self):
        return f'{self.f_name} {self.s_name}'
