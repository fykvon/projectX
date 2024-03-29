# Generated by Django 5.0.2 on 2024-02-22 10:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed', max_length=100, verbose_name='News name')),
                ('text', models.TextField(verbose_name='News text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='News created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='News updated')),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
