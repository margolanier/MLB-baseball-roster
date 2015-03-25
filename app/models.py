from django.db import models
from django.utils import timezone

# Create your models here.

#Team Model
class Team(models.Model):
	name = models.CharField(max_length=50)
	championships = models.IntegerField(null=True)
	hometown = models.CharField(max_length=50, default='')
	ballpark = models.CharField(max_length=50, default='')
	manager = models.CharField(max_length=50, default='')
	owner = models.CharField(max_length=50, default='')
	logo = models.CharField (max_length=300, default='')

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
	weight = models.IntegerField(max_length=3, null=True)
	birthday = models.DateField(default=timezone.now)
	image = models.CharField (max_length=300, default='')

	team = models.ForeignKey('Team', related_name='players')

	class Meta(object):
		ordering = ('number', 'name',)

	def __unicode__(self):
		return u'%s %s' %(self.name, self.number)
