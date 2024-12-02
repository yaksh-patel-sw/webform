from django.db import models

class Registration(models.Model):

        name = models.CharField(max_length=255)
        email = models.EmailField(unique=True)
        phone = models.CharField(max_length=15, unique=True)
        accepted_terms = models.BooleanField()
        view_link = models.URLField(blank=True, null=True)

class Meta:
         app_label= 'formapp'