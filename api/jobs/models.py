from django.db import models
from django.contrib.postgres.fields import ArrayField


class Job(models.Model):
    direct_link = models.CharField(null=True, max_length=300)
    jobsite_link = models.CharField(null=True, max_length=300)
    jobsite = models.CharField(null=True, max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    company = models.CharField(null=True, max_length=300)
    role = models.CharField(null=True, max_length=300)
    tags = ArrayField(models.CharField(max_length=300, null=True), size=10, default=list)