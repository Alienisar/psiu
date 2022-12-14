from django.urls import path

from . import views

app_name = 'esqueleto'
urlpatterns = [
    path('', views.GostosListView.as_view(), name='index'), 
]