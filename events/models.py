from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=600)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=600)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    ticket_required = models.BooleanField(default=False, null=True, blank=True)
    ticket_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name