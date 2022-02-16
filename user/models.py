from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
class Survivor(models.Model):
	name=models.CharField(max_length=200)
	age = models.IntegerField(default=0)
	gender=models.CharField(max_length=30,choices=GENDER_CHOICES)
	username=models.CharField(unique=True,max_length=200)
	last_location = models.CharField(max_length=200)
	water=models.IntegerField(default=0,blank=True)
	food=models.IntegerField(default=0,blank=True)
	medication=models.IntegerField(default=0,blank=True)
	ammunition=models.IntegerField(default=0,blank=True)

	report_count=models.IntegerField(blank=True,default=0)
	is_infected=models.BooleanField(default=False,blank=True)
	date_created = models.DateTimeField(default=timezone.now, blank=True,null=True)


	def has_been_infected(self):
		return (True if self.report_count>=3 else False)
	def survival_level(self):
		return ("{} '%' survival chance ".format((self.water+self.food+self.medication+self.ammunition)/4))

	class Meta:
		ordering = ['-id']
	def __str__(self):
		return (f"{self.name}")
	def get_absolute_url(self):
		return reverse('survivor-detail', kwargs={'pk': self.pk})



CATEGORY_CHOICES = [('Flying', 'Land'), ('Land', 'Land')]
class Robots(models.Model):
	model=models.CharField(max_length=200)
	serialNumber=models.CharField(unique=True, max_length=200)
	manufacturedDate=models.DateTimeField(default=timezone.now)
	category=models.CharField(max_length=30,choices=CATEGORY_CHOICES)

	class Meta:
		ordering = ['-id']
	def __str__(self):
		return (f"{self.model}")

class SurvivorStatistics:
    def __init__(self,infected_survivors, non_infected_survivors):
    	self.total_survivors=infected_survivors+non_infected_survivors
    	self.number_infected=infected_survivors
    	self.number_non_infected=non_infected_survivors
    	self.perc_infected = infected_survivors/(self.total_survivors) if self.total_survivors>0 else 0
    	self.perc_non_infected = non_infected_survivors/self.total_survivors  if self.total_survivors>0 else 0

        

# name, age, gender, ID and last location (latitude, longitude)

 # Water, Food, Medication and Ammunition.
 # model":"1EWDO","serialNumber":"GY8IFJLJXERNY8O","manufacturedDate":"2022-03-06T19:25:39.8638911+00:00","category":"Land