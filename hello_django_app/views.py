from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView (TemplateView):
    template_name = "home.html"

    def get_context_data (self):
        data = {"title" : "Favorite Quote", 
                "quote" : '"In Solitude, I Find My Answers"',
                "anonymous" : "Kristen Butler"
                }
        return data

class AboutPageView (TemplateView):
    template_name = "about.html"

class ContactPageView (TemplateView):
    template_name = "contact.html"
