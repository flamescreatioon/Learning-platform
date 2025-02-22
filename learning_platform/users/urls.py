from django.urls import path
from .views import RegisterView, SubscriptionView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("subscribe/", SubscriptionView.as_view(), name="subscribe")
] 
