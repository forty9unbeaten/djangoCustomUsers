from django.urls import path
from custom_user import views

url_paths = [
    path('', views.homepage_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
