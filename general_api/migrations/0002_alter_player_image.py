# Generated by Django 5.0.2 on 2024-02-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(upload_to='static/player/photo/'),
        ),
    ]
