from django.contrib import admin
from .models import Events

# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'start_date',
        'end_date',
        'start_time',
        'end_time',
        'location',
        'description',
        'image',
        'ticket_required',
    )

    ordering = ('start_date',)

admin.site.register(Events, EventsAdmin)