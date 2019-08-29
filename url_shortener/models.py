from django.db import models


class URL(models.Model):
    url = models.CharField(max_length=255)
    short = models.CharField(max_length=255)
