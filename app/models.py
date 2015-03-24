from django.db import models

# Create your models here.

#Team Model
class Team(models.Model):
	name = models.CharField(unique=True, max_length=50)

	class Meta(object):
		verbose_name_plural = "Teams"
		ordering = ('name',)

	def __unicode__(self):
		return self.name

#Player Model
class Player(models.Model):
	name = models.CharField(max_length=50)
	image = models.TextField()
	number = models.IntegerField(unique=True)
	batsthrows = models.CharField (max_length=50)
	height = models.CharField (max_length=50)
	weight = models.CharField (max_length=50)
	birthday = models.CharField (max_length=50)

	team = models.ForeignKey('Team', related_name='Player')

	class Meta(object):
		ordering = ('number', 'name',)

	def __unicode__(self):
		return u'%s %s' %(self.name, self.number)
