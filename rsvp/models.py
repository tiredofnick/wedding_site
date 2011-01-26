from django.db import models

class Rsvp(models.Model):
	confirmation_code = models.CharField(max_length=60)
	def __unicode__(self):
	        return self.confirmation_code
	
class Attendee(models.Model):
	rsvp = models.ForeignKey(Rsvp)
	name = models.CharField(max_length=60)
	ATTENDING_CHOICES = (
		('1', 'Yes!'),
		('0', 'No, Sorry!'),
	)
	attending = models.CharField(blank=True, max_length=1, choices=ATTENDING_CHOICES)
	MEAL_CHOICES = (
		('0', 'Clambake'),
		('1', 'Vegetarian'),
		('2', 'Chicken')
	)
	meal = models.CharField(blank=True, max_length=1, choices=MEAL_CHOICES)