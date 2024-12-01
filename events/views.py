from django.shortcuts import render

from .models import Events

# Create your views here.
def upcoming_events(request):
    """ View to show upcoming events """

    events = Events.objects.all().order_by('start_date')
    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)