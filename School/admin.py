from django.contrib import admin
from School.models import Contact, Subject, EventImage, Event


class EventImageInline(admin.TabularInline):
    model = EventImage


class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]


admin.site.register(Contact)

admin.site.register(Subject)

admin.site.register(EventImage)

admin.site.register(Event, EventAdmin)


