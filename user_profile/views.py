from django.shortcuts import render, get_object_or_404
from .models import UserProfile

# Create your views here.
def user_profile(request):
    """A view to show the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'user_profile/user_profile.html'
    context={
        'profile':profile,
    }
    return render(request, template, context)
