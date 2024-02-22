from django.contrib import admin

from .models import (Player, Division, Team, )


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["role", "f_name", "s_name", "team", "image"],
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
                "fields": ["name", "slug", "division"],
            },
        ),
    ]
