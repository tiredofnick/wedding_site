from rsvp.models import Rsvp
from rsvp.models import Attendee
from django.contrib import admin

class AttendeeInline(admin.TabularInline):
    model = Attendee
    extra = 3

class RsvpAdmin(admin.ModelAdmin):
    inlines = [AttendeeInline]

admin.site.register(Rsvp, RsvpAdmin)