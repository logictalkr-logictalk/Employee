from django.db import models

# Create your models here.
class Asset(models.Model):
    empid = models.CharField(db_column='empid', max_length=100, blank=False)
    empname = models.CharField(db_column='empname', max_length=100, blank=False)
    asset = models.CharField(db_column='asset', max_length=100, blank=False)
