from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('home/', HomePageView.as_view(), name="home_view"),
    path('about/', AboutPageView.as_view(), name="about_view")
]