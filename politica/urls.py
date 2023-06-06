from django.urls import path

from . import views


app_name = 'politica'

urlpatterns = [
    path('', views.PoliticView.as_view(), name='polit'),
]    