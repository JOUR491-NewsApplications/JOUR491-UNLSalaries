from django.db import models

class Person(models.Model):
    sort_id = models.IntegerField()
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    position_number = models.CharField(max_length=255, blank=True, null=True)
    job_class_number = models.CharField(max_length=255, blank=True, null=True)
    term = models.CharField(max_length=5, blank=True, null=True)
    fte_status = models.FloatField()            
    salary = models.IntegerField()
    def get_absolute_url(self):
        return "http://127.0.0.1:8000/person/%s/" % self.name_slug
    def __unicode__(self):
        return self.name
