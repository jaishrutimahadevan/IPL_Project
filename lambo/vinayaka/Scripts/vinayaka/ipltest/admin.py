from django.contrib import admin
from django.contrib.auth.models import Group
from .models import IplTest,IplTestView,PlayerOfMatchView,teamwins_yearView,IplFinalView
from .models import Profile
from .views import signup_view
# Register your models here.
admin.site.site_header='IPLTEST Administration'
# class IplTestAdmin(admin.ModelAdmin):
	# list_display=('id', 'season', 'city', 'date', 'team1', 'team', 'toss_winner', 'toss_decision', 'result', 'dl_applied','winner', 'win_by_runs', 'win_by_wickets', 'player_of_match', 'venue', 'umpire1', 'umpire')
	# list_filter =('date','season', 'city', 'date','winner','venue')
	# search_fields=('date','season', 'city', 'date','winner','venue')
	# list_per_page=50
# class IplTestViewAdmin(admin.ModelAdmin):
	# list_display=('winner','winner_count')
	# list_filter =('winner','winner_count')

# class PlayerOfMatchViewAdmin(admin.ModelAdmin):
	# list_display=('player_of_match','player_of_match_count')
	# list_filter =('player_of_match','player_of_match_count')

# class teamwins_yearViewAdmin(admin.ModelAdmin):
	# list_display=('season','winner','winner_count')
	# list_filter =('season','winner','winner_count')
	
# class IplFinalViewAdmin(admin.ModelAdmin):
	# list_display=('winner','champion_count')
	# list_filter =('winner','champion_count')


admin.site.register(Profile)
# admin.site.register(IplTest,IplTestAdmin)
# admin.site.register(IplTestView,IplTestViewAdmin)
# admin.site.register(PlayerOfMatchView,PlayerOfMatchViewAdmin)
# admin.site.register(teamwins_yearView,teamwins_yearViewAdmin)
# admin.site.register(IplFinalView,IplFinalViewAdmin)
#admin.site.register(History)
#admin.site.unregister(IplTest)