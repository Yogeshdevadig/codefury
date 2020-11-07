from django.urls import path

from .import views
from job import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
     path('',views.index,name='index'),
     path('about',views.about,name='about'),
     path('register',views.register,name='register'),
     path('login',auth_views.LoginView.as_view(template_name='job/login_s.html'),name='login'),
     path('logout',auth_views.LogoutView.as_view(template_name='job/logout.html'),name='logout'),
     #path('login',views.login_s,name='login'),
]
