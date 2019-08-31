from django.db import models


class URL(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    short = models.CharField(max_length=255)
