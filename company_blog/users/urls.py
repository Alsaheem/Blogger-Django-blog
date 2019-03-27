from django.urls import path
from users import views
from django.conf.urls import url

app_name ='users'

urlpatterns = [
    path('profile/', views.Profile , name='profile'),
]
