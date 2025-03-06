from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'event_host', 'location', 'date_time')
    search_fields = ('title', 'category', 'event_host', 'location')
    list_filter = ('category', 'date_time')
