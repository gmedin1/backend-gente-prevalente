from django.db import models
from django.db.models.fields.files import ImageField
from django.urls.conf import path
from django.conf import settings
from pathlib import Path
# Create your models here.

class Company(models.Model):

    DOCTYPE = [
        ('NIT', 'NIT'),
        ('AT', 'AT'),
        ('ID', 'ID')
    ]

    STATES = [
        ('PENDING', 'PENDING'),
        ('ACCEPTED', 'ACCEPTED'),
        ('REJECTED', 'REJECTED')
    ]

    name = models.CharField(max_length=30)
    detailed = models.CharField(max_length=30)
    doctype = models.CharField(max_length=5, choices=DOCTYPE, default='NIT')
    docnum = models.CharField(max_length=30)
    employees = models.IntegerField()
    logo = models.ImageField()
    state = models.CharField(max_length=10, choices=STATES, default='PENDING')

    def __str__(self):
        return self.name