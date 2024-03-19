from django.contrib import admin

from .models import (Player, Division, Team, )


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["role", "f_name", "s_name", "team", "image", "goals", "yellow_cards", "red_cards", "assists",
                           "games", "missed_goals"],
            },
        ),
    ]


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    fields = 'name', 'year'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "slug", "division", "team_photo", "team_logo", "win", "lose", "draw"],
            },
        ),
    ]
