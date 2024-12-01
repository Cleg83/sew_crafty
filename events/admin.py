from django.contrib import admin
from .models import Events

# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'location',
        'description',
        'image',
        'ticket_required',
    )

    ordering = ('date',)

admin.site.register(Events, EventsAdmin)