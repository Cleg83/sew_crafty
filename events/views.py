from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Events

# Create your views here.
def upcoming_events(request):
    """ View to show upcoming events """

    events = Events.objects.all().order_by('start_date')
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
        if not query:
            messages.error(request, 'Please enter some search criteria!')
            return redirect(reverse('events'))

        queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query)
        events = events.filter(queries)

    context = {
        'events': events,
        'search_criteria': query,
    }

    return render(request, 'events/events.html', context)


