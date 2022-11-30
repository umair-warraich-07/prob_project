# Generated by Django 3.2.16 on 2022-11-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deliveries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ball_id', models.PositiveBigIntegerField(verbose_name='ball_id')),
                ('match_id', models.PositiveIntegerField(verbose_name='match_id')),
                ('inning', models.PositiveIntegerField(verbose_name='inning')),
                ('batting_team', models.CharField(max_length=255, verbose_name='batting_team')),
                ('bowling_team', models.CharField(max_length=255, verbose_name='bowling_team')),
                ('over', models.PositiveIntegerField(verbose_name='over')),
                ('ball', models.PositiveIntegerField(verbose_name='ball')),
                ('batsman', models.CharField(max_length=255, verbose_name='batsman')),
                ('non_stiker', models.CharField(max_length=255, verbose_name='non_stiker')),
                ('bowler', models.CharField(max_length=255, verbose_name='bowler')),
                ('is_super_over', models.PositiveIntegerField(verbose_name='is_super_over')),
                ('wide_runs', models.PositiveIntegerField(verbose_name='wide_runs')),
                ('bye_runs', models.PositiveIntegerField(verbose_name='bye_runs')),
                ('legbye_runs', models.PositiveIntegerField(verbose_name='legbye_runs')),
                ('noball_runs', models.PositiveIntegerField(verbose_name='noball_runs')),
                ('penalty_runs', models.PositiveIntegerField(verbose_name='penalty_runs')),
                ('batsman_runs', models.PositiveIntegerField(verbose_name='batsman_runs')),
                ('extra_runs', models.PositiveIntegerField(verbose_name='extra_runs')),
                ('total_runs', models.PositiveIntegerField(verbose_name='total_runs')),
                ('player_dismissed', models.CharField(max_length=255, verbose_name='player_dismissed')),
                ('dismissal_kind', models.CharField(max_length=255, verbose_name='dismissal_kind')),
                ('fielder', models.CharField(max_length=255, verbose_name='fielder')),
            ],
        ),
    ]