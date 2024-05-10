from django.db import models



class CSVData(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
