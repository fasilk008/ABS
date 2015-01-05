from django.db import models

# Create your models here.

PAGE_TYPE = (('Home', 'Home'), ('Service', 'Service'), ('About', 'About'), ('Faq', 'Faq'))

class Pages(models.Model):
    header = models.CharField(max_length=255,help_text='Header for the page')
    desc = models.CharField(max_length=2000, help_text='Description for the page',blank=True, null=True)
    type = models.CharField(choices=PAGE_TYPE, max_length=7, help_text='Type of the page',unique=True)

    def __unicode__(self):
        return self.type

class Items(models.Model):
	header = models.CharField(max_length=255,help_text='Header for the item' , null=True, blank=True)
	text = models.CharField(max_length=2000, help_text='Text for item')
	image = models.FileField(upload_to='images', null=True, blank=True)
	page = models.ForeignKey(Pages)

# class Photo(models.Model):
#    image    = models.FileField(upload_to='images1', null=True, blank=True, default=None)
#    filename = models.CharField(max_length=60, blank=True, null=True)