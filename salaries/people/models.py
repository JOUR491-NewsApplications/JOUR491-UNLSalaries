from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    title = models.CharField(max_length=255)
    positionNumber = models.CharField(max_length=255)
    jobClassNumber = models.CharField(max_length=255)
    term = models.IntegerField()
    fteStatus = models.FloatField()            
    salary = models.IntegerField()
    def get_absolute_url(self):
        return "/person/%s/" % self.name_slug
    def __unicode__(self):
        return self.name