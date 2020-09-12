from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.views import LogoutView 
from ipltest.views import home_view, signup_view,dashboard_view,loginsuccessful_view,topbatsman_view,topbowlers_view,itenary_view,ipl_ticket_view


urlpatterns = [
    path('', views.home, name='home'),
	
	url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
	url(r'^login/$', LoginView.as_view(template_name= 'login.html'), name='login'),
	url(r'^logout/$',LogoutView.as_view(template_name= 'logged_out.html'), name= 'logout'),
	url(r'^dashboard/$',views.dashboard_view, name= 'dashboard'),
	path('signup/', signup_view, name="signup"),
	url(r'successfullogin/$',views.loginsuccessful_view, name='successfullogin' ),
	url(r'successfullogin/$', views.loginsuccessful_view, name='successfullogin'),
	url(r'topbatsman/$', views.topbatsman_view, name='topbatsman'),
	url(r'topbowlers/$', views.topbowlers_view, name='topbowlers'),
	url(r'tosseffect/$', views.tosswinner_view, name='tosseffect'),
	url(r'firstbatting/$', views.inningscore_view, name='firstbatting'),
	url(r'itenary/$', views.itenary_view, name='itenary'),
	url(r'ipl_ticket/$', views.ticket_buy_view, name='ipl_ticket'),
	#path('', views.home1, name='home'),
   # path('about/', views.about, name='about'),
   # path('delete/<list_id>', views.delete, name='delete'),
   # path('cross_off/<list_id>', views.cross_off, name='cross_off'),
   # path('uncross/<list_id>', views.uncross, name='uncross'),
   # path('edit/<list_id>', views.edit, name='edit'),
] #TemplateView.as_view(template_name='successfulsignup.html'), name='successfulsignup'