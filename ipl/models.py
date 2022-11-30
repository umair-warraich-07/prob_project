from django.db import models

class Deliveries(models.Model):
    match_id= models.PositiveIntegerField(("match_id"))
    inning= models.PositiveIntegerField(("inning"))
    batting_team = models.CharField(("batting_team"),max_length=255)
    bowling_team = models.CharField(("bowling_team"),max_length=255)
    over=models.PositiveIntegerField(("over"))
    ball=models.PositiveIntegerField(("ball"))
    batsman=models.CharField(("batsman"),max_length=255)
    non_stiker=models.CharField(("non_stiker"),max_length=255)
    bowler=models.CharField(("bowler"),max_length=255)
    is_super_over=models.PositiveIntegerField(("is_super_over"))
    wide_runs=models.PositiveIntegerField(("wide_runs"))
    bye_runs=models.PositiveIntegerField(("bye_runs"))
    legbye_runs=models.PositiveIntegerField(("legbye_runs"))
    noball_runs=models.PositiveIntegerField(("noball_runs"))
    penalty_runs=models.PositiveIntegerField(("penalty_runs"))
    batsman_runs=models.PositiveIntegerField(("batsman_runs"))
    extra_runs=models.PositiveIntegerField(("extra_runs"))
    total_runs=models.PositiveIntegerField(("total_runs"))
    player_dismissed=models.CharField(("player_dismissed"),max_length=255)
    dismissal_kind=models.CharField(("dismissal_kind"),max_length=255)
    fielder=models.CharField(("fielder"),max_length=255)


    class Meta:
        verbose_name = "Ball By Ball"
        verbose_name_plural ="Ball by Ball Data"

class Matches(models.Model):
    season=models.CharField(("season"),max_length=255)
    city= models.CharField(("city"),max_length=255)
    date=models.CharField(("date"),max_length=255)
    team1=models.CharField(("team1"),max_length=255)
    team2=models.CharField(("team2"),max_length=255)
    toss_winner= models.CharField(("toss_winner"),max_length=255)
    toss_decision= models.CharField(("toss_decision"),max_length=255)
    result=models.CharField(("result"),max_length=255)
    dl_applied=models.PositiveIntegerField("dl_applied")
    winner=models.CharField(("winner"),max_length=255)
    win_by_runs=models.PositiveIntegerField("win_by_runs")
    win_by_wickets=models.PositiveIntegerField("win_by_wickets")
    player_of_match=models.CharField(("player_of_match"),max_length=255)
    venue=models.CharField(("venue"),max_length=255)
    umpire1=models.CharField(("umpire1"),max_length=255)
    umpire2=models.CharField(("umpire2"),max_length=255)
    class Meta:
        verbose_name = "Match"
        verbose_name_plural ="Matches Data"







