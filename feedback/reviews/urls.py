from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewCreateView.as_view(), name='review'),
    path('thank-you/', views.ThankYouView.as_view(), name='thank_you'),
    path('reviews/', views.ReviewListView.as_view(), name='reviews'),
    path('reviews/<int:pk>/', views.SingleReviewView.as_view(), name='single_review'),
]