from django.db import models
from django.utils import timezone

# Create your models here.

#League Model
class League(models.Model):
	name = models.CharField(max_length=50, null=True)
	logo = models.CharField (max_length=300,  null=True)

	class Meta(object):
		verbose_name_plural = "Leagues"
		ordering = ('name',)

	def __unicode__(self):
		return self.name

#Team Model
class Team(models.Model):
	name = models.CharField(max_length=50)
	championships = models.IntegerField(null=True)
	hometown = models.CharField(max_length=50, null=True, default='')
	ballpark = models.CharField(max_length=50, null=True, default='')
	manager = models.CharField(max_length=50, null=True, default='')
	logo = models.CharField (max_length=300, default='')
	linkToRoster = models.CharField (max_length=300, default='')

	league = models.ForeignKey('League', related_name='teams', null=True)

	class Meta(object):
		verbose_name_plural = "Teams"
		ordering = ('name',)

	def __unicode__(self):
		return self.name

#Player Model
class Player(models.Model):
	name = models.CharField(max_length=50)
	number = models.IntegerField(unique=True)
	position = models.CharField (max_length=50)
	batsthrows = models.CharField (max_length=50)
	height = models.CharField (max_length=50)
	weight = models.IntegerField(max_length=3)
	birthday = models.DateField(default=timezone.now)
	image = models.CharField (max_length=300, default='')

	team = models.ForeignKey('Team', related_name='players')

	class Meta(object):
		ordering = ('number', 'name',)

	def __unicode__(self):
		return u'%s %s' %(self.name, self.number)
