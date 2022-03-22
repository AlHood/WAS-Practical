from django.urls import path
from WASapp import views

app_name = 'WASapp'

urlpatterns = [
    path('', views.index, name='index'),
]
