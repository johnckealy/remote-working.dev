from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
from dateutil.parser import parse


class Job(models.Model):
    direct_link = models.CharField(null=True, max_length=900)
    jobsite_link = models.CharField(null=True, max_length=300)
    jobsite = models.CharField(null=True, max_length=300)
    date = models.DateTimeField(null=True)
    company = models.CharField(null=True, max_length=300)
    role = models.CharField(null=True, max_length=300)
    tags = ArrayField(models.CharField(max_length=300, null=True), size=10, default=list)

    @property
    def datef(self):
        if datetime.now().year == self.date.year:
            return datetime.strftime(self.date, '%d %b')
        else:
            return datetime.strftime(self.date, '%d %b, %Y')