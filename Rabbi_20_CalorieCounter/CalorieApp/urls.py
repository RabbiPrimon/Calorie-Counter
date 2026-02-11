from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_consumption/', views.add_consumption, name='add_consumption'),
    path('logout/', views.logout_view, name='logout'),
]
