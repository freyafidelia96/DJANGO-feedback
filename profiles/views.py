from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import UserProfile

# Create your views here.


class CreateProfile(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"
    
    
class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"