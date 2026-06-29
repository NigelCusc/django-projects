from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),
    path('thank-you/', views.thank_you, name='thank_you'),
]