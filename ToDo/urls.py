from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('add/', views.add, name="add"),
    path('delete/<int:key_id>', views.delete, name="delete"),
]
