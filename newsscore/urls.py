from django.urls import path
from .views import get_articles
from newsscore import views


urlpatterns = [
    path('',views.home, name='home'),
    path('news.html/',views.news, name='news'),
    path('signup.html/',views.signup, name='signup'),
    path('get_articles/', get_articles, name='get_articles'),
    path('login.html/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
]
