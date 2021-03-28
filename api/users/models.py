from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    include_chips = ArrayField(models.CharField(max_length=300, null=True), default=list, size=60)
    ignore_chips = ArrayField(models.CharField(max_length=300, null=True), default=list, size=60)
    include_tag_chips = ArrayField(models.CharField(max_length=300, null=True), default=list, size=60)
    ignore_tag_chips = ArrayField(models.CharField(max_length=300, null=True), default=list, size=60)


