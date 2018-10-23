from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView (TemplateView):
    template_name = "home.html"

    def get_context_data (self):
        data = {"message_title" : "Yahoo!", "message" : "Django is Great!"}
        return data

class AboutPageView (TemplateView):
    template_name = "about.html"