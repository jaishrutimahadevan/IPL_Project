from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.dispatch import dispatcher
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import Settings
from .signals import object_viewed_signal

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)

def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def update_profile_signal(sender, instance, created, **kwargs):

	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
	
class IplTest(models.Model):
   season = models.IntegerField()
   city = models.CharField(max_length=255, blank=True, null=True)
   date = models.DateField(blank=True, null=True)
   team1 = models.CharField(max_length=255, blank=True, null=True)
   team = models.CharField(max_length=255, blank=True, null=True)
   toss_winner = models.CharField(max_length=255, blank=True, null=True)
   toss_decision = models.CharField(max_length=255, blank=True, null=True)
   result = models.CharField(max_length=255, blank=True, null=True)
   dl_applied = models.IntegerField(blank=True, null=True)
   winner = models.CharField(max_length=255, blank=True, null=True)
   win_by_runs = models.IntegerField(blank=True, null=True)
   win_by_wickets = models.IntegerField(blank=True, null=True)
   player_of_match = models.CharField(max_length=255, blank=True, null=True)
   venue = models.CharField(max_length=255, blank=True, null=True)
   umpire1 = models.CharField(max_length=255, blank=True, null=True)
   umpire = models.CharField(max_length=255, blank=True, null=True)
   umpire3 = models.CharField(max_length=255, blank=True, null=True)

   class Meta:
      managed = False
      db_table = 'ipl_test'
	  
class IplTestView(models.Model):
	winner = models.CharField(max_length=255)
	winner_count = models.DecimalField(max_digits=19, decimal_places=0)
 
	class Meta:
		managed = False
		db_table = 'ipl_testview'
		
class PlayerOfMatchView(models.Model):
	player_of_match = models.CharField(max_length=255)
	player_of_match_count = models.DecimalField(max_digits=19, decimal_places=0)
 
	class Meta:
		managed = False
		db_table = 'player_of_match_view'
		
class teamwins_yearView(models.Model):
    season = models.CharField(max_length=255)
    winner = models.CharField(max_length=255)
    winner_count = models.DecimalField(max_digits=19, decimal_places=0)

    class Meta:

        managed= False
        db_table='teamwins_year'

class IplFinalView(models.Model):
    winner = models.CharField(max_length=255)
    champion_count = models.DecimalField(max_digits=19, decimal_places=0)

    class Meta:

        managed= False
        db_table='iplfinal_view'
		
class topbatsmanview(models.Model):
	POS = models.DecimalField(max_digits=19, decimal_places=0)
	PLAYER_NAME = models.CharField(max_length=255)
	MATCHES = models.DecimalField(max_digits=19, decimal_places=0)
	INNS = models.DecimalField(max_digits=19, decimal_places=0)
	NOTOUT = models.DecimalField(max_digits=19, decimal_places=0)
	RUNS = models.DecimalField(max_digits=19, decimal_places=0)
	HIGEST_SCORE = models.DecimalField(max_digits=19, decimal_places=0)
	AVERAGE = models.DecimalField(max_digits=19, decimal_places=2)
	BF = models.DecimalField(max_digits=19, decimal_places=0)
	STRIKERATE = models.DecimalField(max_digits=19, decimal_places=2)
	HUNDREDS = models.DecimalField(max_digits=19, decimal_places=0)
	FIFTIES = models.DecimalField(max_digits=19, decimal_places=0)
	FOURS = models.DecimalField(max_digits=19 ,decimal_places=0)
	SIXES = models.DecimalField(max_digits=19, decimal_places=0) 
	
	class Meta:
		managed = False
		db_table = 'topbatsman_view'
		
class topbowlersview(models.Model):
	id = models.AutoField(primary_key=True)
	POS = models.DecimalField(max_digits=19, decimal_places=0)
	PLAYER_NAME = models.CharField(max_length=255)
	MATCHES = models.DecimalField(max_digits=19, decimal_places=0)
	INNS = models.DecimalField(max_digits=19, decimal_places=0)
	OVER = models.DecimalField(max_digits=19, decimal_places=0)
	RUNS = models.DecimalField(max_digits=19, decimal_places=0)
	WICKETS = models.DecimalField(max_digits=19, decimal_places=0)
	BBI = models.DecimalField(max_digits=19, decimal_places=2)
	AVERAGE = models.DecimalField(max_digits=19, decimal_places=2)
	ECONOMY = models.DecimalField(max_digits=19, decimal_places=2)
	STRIKERATE = models.DecimalField(max_digits=19, decimal_places=2)
	FOUR_WIKETS = models.DecimalField(max_digits=19, decimal_places=0)
	FIVE_WICKETS = models.DecimalField(max_digits=19 ,decimal_places=0)
	
	
	class Meta:
		managed = False
		db_table = 'topbowlers_view'

class deliveries(models.Model):
   match_id = models.IntegerField()
   inning = models.IntegerField(blank=True, null=True)
   batting_team = models.CharField(max_length=255, blank=True, null=True)
   bowling_team = models.CharField(max_length=255, blank=True, null=True)
   over = models.IntegerField(blank=True, null=True)
   ball = models.IntegerField(blank=True, null=True)
   batsman = models.CharField(max_length=255, blank=True, null=True)
   non_striker = models.CharField(max_length=255, blank=True, null=True)
   bowler = models.CharField(max_length=255, blank=True, null=True)
   is_super_over = models.IntegerField(blank=True, null=True)
   wide_runs = models.IntegerField(blank=True, null=True)
   bye_runs = models.IntegerField(blank=True, null=True)
   legbye_runs = models.IntegerField(blank=True, null=True)
   noball_runs = models.IntegerField(blank=True, null=True)
   penalty_runs = models.IntegerField(blank=True, null=True)
   batsman_runs = models.IntegerField(blank=True, null=True)
   extra_runs = models.IntegerField(blank=True, null=True)
   total_runs =models.IntegerField(blank=True, null=True)
   player_dismissed = models.CharField(max_length=255, blank=True, null=True)
   dismisal_kind = models.CharField(max_length=255, blank=True, null=True)
   fielder = models.CharField(max_length=255, blank=True, null=True)
   wicket = models.IntegerField(blank=True, null=True)
   matchid = models.CharField(max_length=255, blank=True, null=True)

   class Meta:
      managed = False
      db_table = 'deliveries'	

class inningscore_View(models.Model):
   id = models.AutoField(primary_key=True)
   firstinning_score = models.IntegerField(blank=True, null=True)
   secondinning_score = models.IntegerField(blank=True, null=True)
    
   class Meta:
        managed= False
        db_table='inningscore_view'
		
class Itenary(models.Model):
   id = models.AutoField(primary_key=True)
   Teams = models.CharField(max_length=255, blank=True, null=True)
   Date = models.DateField(blank=True, null=True)
   Day = models.CharField(max_length=255, blank=True, null=True)
   Time = models.CharField(max_length=255, blank=True, null=True)
   Venue = models.CharField(max_length=255, blank=True, null=True)

   class Meta:
      managed = False
      db_table = 'ipl_itenary'

class MatchID(models.Model):
	M_ID = models.IntegerField(blank=True, null=True)
	class Meta:
		managed= True
		db_table='ipl_matchid'
