from django.urls import path
from . import views

urlpatterns = [
    path('', views.response_home_gallery, name="home"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register_user, name="register"),
    path('logout/', views.logout_user, name="logout"),
    path('upload/', views.upload_picture, name='upload_picture'),
]