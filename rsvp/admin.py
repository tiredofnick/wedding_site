from rsvp.models import Rsvp
from rsvp.models import Attendee
from rsvp.models import Meal
from django.contrib import admin

# admin.site.register(Rsvp)
# admin.site.register(Attendee)
# admin.site.register(Meal)

class AttendeeInline(admin.ModelAdmin):
    model = Attendee
    extra = 3

class RsvpAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['confirmation_code']}),
    ]
    inlines = [AttendeeInline]

admin.site.register(Rsvp, RsvpAdmin)