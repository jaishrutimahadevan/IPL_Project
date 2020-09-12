from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from .models import IplTest,IplTestView,PlayerOfMatchView,teamwins_yearView,IplFinalView,topbatsmanview,topbowlersview,deliveries,inningscore_View,Itenary,MatchID
from .forms import IplTestForm,IplTestViewForm,PlayerOfMatchViewForm,teamwins_yearViewForm,IplFinalViewForm,topbatsmanviewForm,topbowlersviewForm,inningscoreViewForm,ItenaryForm,MatchIDForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from plotly.offline import plot
from plotly.graph_objs import Scatter
from plotly.graph_objs import pie
from plotly.graph_objs import layout
import plotly.graph_objs as go
from django.http import HttpResponse
from django.db.models import Count, F, Value, Sum,Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import signup_viewForm
#import matplotlib.pyplot as plt

def home_view(request):
		return render(request, "home.html")
		
def ipl_ticket_view(request):
		
		return render(request, "ipl_ticket.html")

def signup_view(request):
	form = signup_viewForm(request.POST)
	if form.is_valid():
		user = form.save()
		user.profile.first_name = form.cleaned_data.get('first_name')
		user.profile.last_name = form.cleaned_data.get('last_name')
		user.profile.email = form.cleaned_data.get('email')
		#user.profile.bio = form.cleaned_data.get('bio')
		user.save()
		profile = user.profile
		profile.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		
		user.refresh_from_db()
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('successfullogin')
	else:
		form= signup_viewForm()
	return render(request,'signup.html',{'form':form})

def home(request):
		return render(request, "home.html")
def dashboard_view(request):
		# return render(request, "dashboard.html")
		# return redirect('dashboard')
		winner_count=IplTestView.objects.all()
		champion_count=IplFinalView.objects.all()
		go.layout.legend.bgcolor = '#E2E2E2'
		season_winner_count= teamwins_yearView.objects.filter(winner='Mumbai Indians').order_by('season')
		season_winner_count1= teamwins_yearView.objects.filter(winner='Chennai Super Kings').order_by('season')
		season_winner_count2= teamwins_yearView.objects.filter(winner='Kolkata Knight Riders').order_by('season')
		
		x=[]
		y=[]
		x1=[]
		y1=[]
		x2=[]
		y2=[]
		qs4 = season_winner_count.values_list('season',flat=True)
		for e4 in qs4:
		
		    x.append(e4)
		qs6 = season_winner_count1.values_list('season',flat=True)
		for e6 in qs6:
		
		    x1.append(e6)
		qs8 = season_winner_count2.values_list('season',flat=True)
		for e8 in qs8:
		
		    x2.append(e8)
		
		qs5 = season_winner_count.values_list('winner_count',flat=True)
		for e5 in qs5:
		
		    y.append(e5)
		qs7 = season_winner_count1.values_list('winner_count',flat=True)
		for e7 in qs7:
		
		    y1.append(e7)
		qs9 = season_winner_count2.values_list('winner_count',flat=True)
		for e9 in qs9:
		
		    y2.append(e9)
		
	#   langs = ['C', 'C++', 'Java', 'Python', 'PHP']		
		qs = winner_count.values_list('winner',flat=True)
		langs=[]
		students=[]
		for e in qs:
		
		    langs.append(e)
			
		qs1=winner_count.values_list('winner_count',flat=True)
		
		for e1 in qs1:
		
		    students.append(e1)			
		
		trace = go.Pie(labels = langs, values = students)
		
		data = [trace]
		
		# trace.title="TOP FIVE TEAMS"
		# trace.title.font.family='Times New Roman'
		# trace.title.font.size=25
		# trace.title.font.color='#006600'
		# trace.title.position="bottom center"
		# trace.marker.colors=['blue','yellow','#29235f','#e92e06','red']
		playerofmatch_count=PlayerOfMatchView.objects.all()
		qs2 = playerofmatch_count.values_list('player_of_match',flat=True)
		langs1=[]
		students1=[]
		for e2 in qs2:
		
		    langs1.append(e2)
			
		qs3=playerofmatch_count.values_list('player_of_match_count',flat=True)
		
		for e3 in qs3:
		
		    students1.append(e3)			

		trace1 = go.Pie(labels = langs1, values = students1)
		data1 = [trace1]
		
		trace1.title="TOP FIVE MAN OF THE MATCH"
		trace1.title.font.family='Times New Roman'
		trace1.title.font.size=25
		trace1.title.font.color='#006600'
		trace1.title.position="bottom center"
		trace1.marker.colors=['#e92e06','#29235f','e25e12','#e92e06','blue']
		#trace.pull=0.1
		#trace.domain.x=[0,0.4]
		#trace.domain.y=[0,1]
		#trace.showlegend=False
		trace2 = go.Scatter(x=x,y=y)
		trace3 = go.Scatter(x=x1,y=y1)
		trace4 = go.Scatter(x=x2,y=y2)
		data2 = [trace2,trace3,trace4]
		#data3 = [trace3]
		trace2.name="Mumbai Indians"
		
		trace3.name="Chennai Super Kings"
		
		trace4.name="Kolkata Knight Riders"
		
		trace2.marker.colorbar.title="YEAR VS WIN"
		trace2.showlegend=True
		trace2.marker.showscale=False
		# trace2.marker.colorbar.title.font.family='Times New Roman'
		# trace2.marker.colorbar.title.font.size=25
		# trace2.marker.colorbar.title.side ="bottom"
		# #trace2.marker.colorbar.title.position="bottom center"
		plot_div = plot(go.Figure(data = data),output_type='div')
		
		
		plot_div1=plot(go.Figure(data = data1),output_type='div')
		layout=go.Layout(title="YEAR VS WIN",xaxis={'title':'YEAR'}, yaxis={'title':'WIN'})
		fig = go.Figure(data = data2,layout=layout)
		fig.update_layout(title={'text': "YEAR VS WIN",'font.size':25,'y':0.8,'x':0.4,'xanchor': 'center','yanchor': 'bottom'})
		plot_div2=plot(fig,output_type='div')
		
		#iplot(fig)		
		all_items = IplTest.objects.all().order_by('season')
		paginator = Paginator(all_items,5)
		page= request.GET.get('page',1)		
		
		try:
			allitems= paginator.page(page)
		except PageNotAnInteger:
			allitems= paginator.page(1)
		except (EmptyPage,InvalidPage):
			allitems= paginator.page(1)
		
		index = allitems.number - 1  # edited to something easier without index    
		
    # You want a range of 7, so lets calculate where to slice the list
				
		
		# This value is maximum index of your pages, so the last page - 1
		max_index = len(paginator.page_range)
		start_index = index - 3 if index >= 3 else 0
		end_index = index + 3 if index <= max_index - 3 else max_index
		page_range = list(paginator.page_range)[start_index:end_index]
		context = {'plot_div': plot_div,'plot_div1': plot_div1,'plot_div2': plot_div2, 'allitems': allitems,'max_index': max_index,'page_range': page_range,'winner_count': winner_count,'champion_count':champion_count}
		return render(request, "dashboard.html", context)

# Create your views here.


def loginsuccessful_view(request):
		# return render(request, "dashboard.html")
		# return redirect('dashboard')
		winner_count=IplTestView.objects.all()
		
		#go.layout.legend.bgcolor = '#E2E2E2'
		season_winner_count= teamwins_yearView.objects.filter(winner='Mumbai Indians').order_by('season')
		season_winner_count1= teamwins_yearView.objects.filter(winner='Chennai Super Kings').order_by('season')
		season_winner_count2= teamwins_yearView.objects.filter(winner='Kolkata Knight Riders').order_by('season')
		
		x=[]
		y=[]
		x1=[]
		y1=[]
		x2=[]
		y2=[]
		qs4 = season_winner_count.values_list('season',flat=True)
		for e4 in qs4:
		
		    x.append(e4)
		qs6 = season_winner_count1.values_list('season',flat=True)
		for e6 in qs6:
		
		    x1.append(e6)
		qs8 = season_winner_count2.values_list('season',flat=True)
		for e8 in qs8:
		
		    x2.append(e8)
		
		qs5 = season_winner_count.values_list('winner_count',flat=True)
		for e5 in qs5:
		
		    y.append(e5)
		qs7 = season_winner_count1.values_list('winner_count',flat=True)
		for e7 in qs7:
		
		    y1.append(e7)
		qs9 = season_winner_count2.values_list('winner_count',flat=True)
		for e9 in qs9:
		
		    y2.append(e9)
		
	#   langs = ['C', 'C++', 'Java', 'Python', 'PHP']		
		qs = winner_count.values_list('winner',flat=True)
		
		langs=[]
		langs_histo=[]
		students=[]
		students_histo=[]
		for e in qs:
		
		    langs.append(e)
		
			
		qs1=winner_count.values_list('winner_count',flat=True)
		
		
		for e1 in qs1:
		
		    students.append(e1)
				
		
		trace = go.Pie(labels = langs, values = students)
		
		data = [trace]
		
		
		trace.marker.colors=['blue','yellow','#29235f','#e92e06','red']
		# #trace_bar.marker.colors=['blue','yellow','#29235f','#e92e06','red']
		trace.title="TOP FIVE TEAMS"
		trace.title.font.family='Times New Roman'
		trace.title.font.size=25
		trace.title.font.color='#006600'
		trace.title.position="bottom center"
		#trace_bar.name="Team Wins"
		#trace_bar.showlegend=False
		#trace_bar.marker.color='#a7a760'
		
			
		#trace_bar.marker.colorbar.title.font.size=25
		#trace_bar.marker.colorbar.title.font.color='#006600'
		#trace_bar.marker.colorbar.title.side="bottom"
		playerofmatch_count=PlayerOfMatchView.objects.all()
	#   langs = ['C', 'C++', 'Java', 'Python', 'PHP']		
		qs2 = playerofmatch_count.values_list('player_of_match',flat=True)
		langs1=[]
		students1=[]
		for e2 in qs2:
		
		    langs1.append(e2)
			
		qs3=playerofmatch_count.values_list('player_of_match_count',flat=True)
		
		for e3 in qs3:
		
		    students1.append(e3)			

		trace1 = go.Pie(labels = langs1, values = students1)
		data1 = [trace1]
		
		trace1.title="TOP FIVE MAN OF THE MATCH"
		trace1.title.font.family='Times New Roman'
		trace1.title.font.size=25
		trace1.title.font.color='#006600'
		trace1.title.position="bottom center"
		trace1.marker.colors=['#e92e06','#29235f','e25e12','#e92e06','blue']
		#trace.pull=0.1
		#trace.domain.x=[0,0.4]
		#trace.domain.y=[0,1]
		#trace.showlegend=False
		trace2 = go.Scatter(x=x,y=y,mode='markers+lines')
		trace3 = go.Scatter(x=x1,y=y1,mode='markers+lines')
		trace4 = go.Scatter(x=x2,y=y2,mode='markers+lines')
		trace5 = go.Bar(x=x,y=y)
		trace6 = go.Bar(x=x1,y=y1)
		trace7 = go.Bar(x=x2,y=y2)
		data2 = [trace2,trace3,trace4]
		data_bar =[trace5,trace6,trace7]
		#data3 = [trace3]
		trace5.name="Mumbai Indians"
		trace6.name="Chennai Super Kinds"
		trace7.name="Kolkata Knight Riders"
		trace5.marker.line.color='#FEA47F'
		trace6.marker.line.color='#F97F51'
		trace7.marker.line.color='#B33771'
		trace2.name="Mumbai Indians"
		trace2.marker.line.color='#e92e06'
		trace3.name="Chennai Super Kings"
		trace3.marker.line.color='#29235f'
		trace4.name="Kolkata Knight Riders"
		trace4.marker.line.color='#e92e06'
		trace2.marker.colorbar.title="YEAR VS WIN"
		trace2.showlegend=True
		trace2.marker.showscale=False
		plot_div = plot(go.Figure(data = data),output_type='div')
		layout_bar = go.Layout(title={'text':'Top Team Wins/year','font.size':25,'y':0.8,'x':0.4,'xanchor':'center', 'yanchor':'bottom',},barmode='stack' , plot_bgcolor = '#2a4d69')
		plot_bar_div=plot(go.Figure(data=data_bar,layout=layout_bar),output_type='div')
		
		plot_div1=plot(go.Figure(data = data1),output_type='div')
		layout=go.Layout(title="YEAR VS WIN",xaxis={'title':'YEAR'}, yaxis={'title':'WIN'})
		fig = go.Figure(data = data2,layout=layout)
		fig.update_layout(title={'text': "YEAR VS WIN",'font.size':25,'y':0.8,'x':0.4,'xanchor': 'center','yanchor': 'bottom'})
		plot_div2=plot(fig,output_type='div')
		
		#iplot(fig)		
		
		context = {'plot_div': plot_div,'plot_div1': plot_div1,'plot_div2': plot_div2,'plot_bar_div':plot_bar_div}
		return render(request, "successfullogin.html", context)
def topbatsman_view(request):
		topbat_items = topbatsmanview.objects.all()
		# paginator_topbat = Paginator(topbat_items,5)
		# page_topbat= request.GET.get('page',1)		
		
		# try:
			# allitems_topbat= paginator_topbat.page(page)
		# except PageNotAnInteger:
			# allitems_topbat= paginator_topbat.page(1)
		# except (EmptyPage,InvalidPage):
			# allitems_topbat= paginator_topbat.page(1)
		
		# index_topbat = allitems_topbat.number - 1  # edited to something easier without index    
		
    # # You want a range of 7, so lets calculate where to slice the list
				
		
		# # This value is maximum index of your pages, so the last page - 1
		# max_index_topbat = len(paginator_topbat.page_range)
		# start_index_topbat = index_topbat - 3 if index_topbat >= 3 else 0
		# end_index_topbat= index_topbat + 3 if index_topbat <= max_index_topbat - 3 else max_index_topbat
		# page_range_topbat = list(paginator_topbat.page_range)[start_index_topbat:end_index_topbat]
		context = {'topbat_items':topbat_items}
		return render(request, "topbatsman.html", context)
def topbowlers_view(request):
		topbowl_items = topbowlersview.objects.all()
		# paginator_topbat = Paginator(topbat_items,5)
		# page_topbat= request.GET.get('page',1)		
		
		# try:
			# allitems_topbat= paginator_topbat.page(page)
		# except PageNotAnInteger:
			# allitems_topbat= paginator_topbat.page(1)
		# except (EmptyPage,InvalidPage):
			# allitems_topbat= paginator_topbat.page(1)
		
		# index_topbat = allitems_topbat.number - 1  # edited to something easier without index    
		
    # # You want a range of 7, so lets calculate where to slice the list
				
		
		# # This value is maximum index of your pages, so the last page - 1
		# max_index_topbat = len(paginator_topbat.page_range)
		# start_index_topbat = index_topbat - 3 if index_topbat >= 3 else 0
		# end_index_topbat= index_topbat + 3 if index_topbat <= max_index_topbat - 3 else max_index_topbat
		# page_range_topbat = list(paginator_topbat.page_range)[start_index_topbat:end_index_topbat]
		context = {'topbowl_items':topbowl_items}
		return render(request, "topbowlers.html", context)
		
def tosswinner_view(request):
		
		qs =IplTest.objects.all().filter(toss_winner=F('winner'))
		wincount=len(qs)
		qs1 =IplTest.objects.all().exclude(toss_winner=F('winner'))
		losscount=len(qs1)
		name=['win','loss']
		toss_effect=[wincount,losscount]
		trace1 = go.Pie(labels = name, values = toss_effect)
		data1 = [trace1]
		trace1.title="TOSS EFFECT ON RESULT"
		trace1.title.font.family='Times New Roman'
		trace1.title.font.size=25
		trace1.title.font.color='#006600'
		trace1.title.position="bottom center"
		trace1.marker.colors=['#0e0fed','#8bf0ba']
		trace1.marker.colors=['#3a4660','#845007']		
		plot_div_toss=plot(go.Figure(data = data1),output_type='div')
		qs2 =IplTest.objects.all().filter(toss_decision='bat').exclude(win_by_runs='0')
		bat_win=len(qs2)
		qs3 =IplTest.objects.all().filter(toss_decision='bat')
		bat_loss=len(qs3)-bat_win
		name=['bat_win','bat_loss']
		toss_effect=[bat_win,bat_loss]
		trace2 = go.Pie(labels = name, values = toss_effect)
		trace2.title="TOSS DECISION BAT"
		trace2.title.font.family='Times New Roman'
		trace2.title.font.size=25
		trace2.title.font.color='#006600'
		trace2.title.position="bottom center"
		trace2.marker.colors=['#F7882F','#6B7A8F']
		data2 = [trace2]	
		plot_div_decision=plot(go.Figure(data = data2),output_type='div')
		qs4 =IplTest.objects.all().filter(toss_decision='field')& IplTest.objects.all().filter(toss_winner=F('winner'))
		bowl_win=len(qs4)
		qs5 =IplTest.objects.all().filter(toss_decision='field')
		bowl_loss=len(qs5)-bowl_win
		name=['bowl_win','bowl_loss']
		toss_effect=[bowl_win,bowl_loss]
		trace3 = go.Pie(labels = name, values = toss_effect)
		data3 = [trace3]
		trace3.title="TOSS DECISION BOWL"
		trace3.title.font.family='Times New Roman'
		trace3.title.font.size=25
		trace3.title.font.color='#006600'
		trace3.title.position="bottom center"
		trace3.marker.colors=['#e1b382','#2d545e']
		plot_div_decision1=plot(go.Figure(data = data3),output_type='div')
		
		context = {'plot_div_toss':plot_div_toss,'plot_div_decision':plot_div_decision,'plot_div_decision1':plot_div_decision1}
		return render(request, "tosseffect.html", context)
		
def inningscore_view(request):
		
		#qs1 =inningscore_View.objects.all().filter(firstinning_score_gt'=150) & deliveries.objects.all().filter(firstinning_score_gt=F('secondinning_score'))
		qs1 =inningscore_View.objects.all().raw("select id,firstinning_score from inningscore_View where firstinning_score>'150' and firstinning_score>secondinning_score")
		bat_win=len(qs1)
		qs2 =inningscore_View.objects.all().raw("select id,firstinning_score from inningscore_View where firstinning_score>'150' and firstinning_score<secondinning_score")
		bat_loss=len(qs2)
		name=['bat_win','bat_loss']
		run_effect=[bat_win,bat_loss]
		trace3 = go.Pie(labels = name, values = run_effect)
		data3 = [trace3]
		trace3.title=" FIRST INNING SCORE>150"
		trace3.title.font.family='Times New Roman'
		trace3.title.font.size=25
		trace3.title.font.color='#006600'
		trace3.title.position="bottom center"
		trace3.marker.colors=['#e1b382','#2d545e']
		plot_div_decision2=plot(go.Figure(data = data3),output_type='div')
		qs3 =inningscore_View.objects.all().raw("select id,firstinning_score from inningscore_View where firstinning_score>'200' and firstinning_score>secondinning_score")
		bat1_win=len(qs3)
		qs4 =inningscore_View.objects.all().raw("select id,firstinning_score from inningscore_View where firstinning_score>'200' and firstinning_score<secondinning_score")
		bat1_loss=len(qs4)
		name=['bat_win','bat_loss']
		run1_effect=[bat1_win,bat1_loss]
		trace4 = go.Pie(labels = name, values = run1_effect)
		data4 = [trace4]
		trace4.title=" FIRST INNING SCORE>200"
		trace4.title.font.family='Times New Roman'
		trace4.title.font.size=25
		trace4.title.font.color='#006600'
		trace4.title.position="bottom center"
		trace4.marker.colors=['#e1b382','#2d545e']
		plot_div_decision3=plot(go.Figure(data = data4),output_type='div')
		
		# qs4 =IplTest.objects.all().values('season').filter('win_by_runs'!=0).annotate(total=Count('id')) 
		# #qs5 =IplTest.objects.all().raw("select id,season,count(win_by_runs) as firstbattingwin from ipl_test where win_by_runs!=0 group by season")
		# x=[]
		# y=[]
		# for e4 in qs4[0]:
		
		    # x.append(e4)
		# for e5 in qs4[1]:
		
		    # y.append(e5)
		# trace_bar1 = go.scatter(x=x,y=y,mode='markers+lines')
		# data_bar1= trace_bar1
		# layout_bar1 = go.Layout(title={'text':'BAT VS BOWL','font.size':25,'y':0.8,'x':0.4,'xanchor':'center', 'yanchor':'bottom',},barmode='stack' , plot_bgcolor = '#2a4d69')
		# plot_div_bar1=plot(go.Figure(data=data_bar1,layout=layout_bar1),output_type='div')
		context = {'plot_div_decision2':plot_div_decision2,'plot_div_decision3':plot_div_decision3}
		
		return render(request, "firstbatting.html", context)


def itenary_view(request):
	itenitems = Itenary.objects.all()
	context = {'itenitems': itenitems}
	return render(request, "itenary.html", context)
def ticket_buy_view(request):
	if request.method=="GET":
		query=request.GET.get('txt',None)
		
		qs1 =Itenary.objects.all().raw("select id,Teams,Date,Day,Time,Venue from ipl_Itenary where id ="+query)
		context={'query':query,'qs1':qs1}
		return render(request, "ipl_ticket.html",context)

