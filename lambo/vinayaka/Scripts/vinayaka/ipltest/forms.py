from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import IplTest,IplTestView,PlayerOfMatchView,teamwins_yearView,IplFinalView,topbatsmanview,topbowlersview,deliveries,inningscore_View,Itenary,MatchID
 
class signup_viewForm(UserCreationForm):
	
	username = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=200)	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')
 
class IplTestForm(forms.ModelForm):
    class Meta:
        model = IplTest
        fields = ["id", "season", "city", "date", "team1", "team", "toss_winner", "toss_decision", "result", "dl_applied",	"winner", "win_by_runs", "win_by_wickets", "player_of_match", "venue", "umpire1", "umpire"]

class IplTestViewForm(forms.ModelForm):
    class Meta:
        model = IplTestView
        fields = ["winner","winner_count"]
		
class PlayerOfMatchViewForm(forms.ModelForm):
    class Meta:
        model = PlayerOfMatchView
        fields = ["player_of_match","player_of_match_count"]

class teamwins_yearViewForm(forms.ModelForm):
    class Meta:
        model = teamwins_yearView
        fields = ["season","winner","winner_count"]

class IplFinalViewForm(forms.ModelForm):
    class Meta:
        model = IplFinalView
        fields = ["winner","champion_count"]

class topbatsmanviewForm(forms.ModelForm):
    class Meta:
        model = topbatsmanview
        fields = ["POS","PLAYER_NAME","MATCHES","INNS","NOTOUT","RUNS","HIGEST_SCORE","AVERAGE","BF","STRIKERATE","HUNDREDS","FIFTIES","FOURS","SIXES"]

class topbowlersviewForm(forms.ModelForm):
    class Meta:
        model = topbowlersview
        fields = ["POS","PLAYER_NAME","MATCHES","INNS","OVER","RUNS","WICKETS","BBI","AVERAGE","ECONOMY","STRIKERATE","FOUR_WIKETS","FIVE_WICKETS"]

class deliveriesForm(forms.ModelForm):		
	class Meta:
		model = deliveries
		fields = ["match_id","inning","batting_team","bowling_team", "over","ball","batsman","non_striker","bowler","is_super_over","wide_runs","bye_runs","legbye_runs","noball_runs","penalty_runs","batsman_runs","extra_runs","total_runs", "player_dismissed","dismisal_kind","fielder","wicket", "matchid"]

class inningscoreViewForm(forms.ModelForm):
    class Meta:
        model = inningscore_View
        fields = ["firstinning_score","secondinning_score"]

class ItenaryForm(forms.ModelForm):
    class Meta:
        model = Itenary
        fields = ["id","Teams","Date","Day","Time","Venue"]
class MatchIDForm(forms.Form):
   class Meta:
        model = MatchID
        fields = ["M_ID"]
    