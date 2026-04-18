from django.urls import path

from . import views

app_name = 'challenges'

urlpatterns = [
    path('<int:month_number>/', views.month_numeric_redirect, name='month_by_number'),
    path('<str:month>/', views.monthly_challenge, name='month'),
]
